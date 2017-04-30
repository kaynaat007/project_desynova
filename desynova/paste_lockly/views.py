from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.core.urlresolvers import reverse

# Create your views here.
from .forms import MessageForm, ReadMessageForm
from .utils import encode, decode, check_key_size_bytes
from .models import Message
import desynova.errors as errors

# There is one loop hole. The key is stored as raw key in the database. anyone with access to database can use the key and
# decrypt the message. Ideally all keys should be encrypted with a common key which should be kep somewhere else.


class MessageView(View):
    """
    The View which displays the Form where user will input the message and an optional secret key
    """
    form_class = MessageForm
    template_name = 'message.html'
    initial = {}

    def get(self, request, *args, **kwargs):
        """
        :param request: the HttpRequest object
        :param args: list of args
        :param kwargs: key word args
        :return: a form which displays a text box and a place for entering secret key
        """
        try:
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})
        except Exception as e:
            return HttpResponseBadRequest(errors.STANDARD_ERROR_TEMPLATE.format(e.args or e.message))

    def post(self, request):
        """
        The code that handles the POST request
        :param request:
        :return: receives the message in the box and secret key ( if any ) and then applies AES to encrypt the message and
        store in database. The message is always stored in encrypted format if the key is provided.
        """
        try:
            form = self.form_class(request.POST)
            if form.is_valid():
                # get the message
                message = form.cleaned_data['message']
                # we do not proceed if we don't get any message
                if not message:
                    return HttpResponseBadRequest("Please provide non null values in message box")
                # get the secret key
                secret_key = form.cleaned_data['secret_key']

                # create an object each time you receive something in message and form is valid
                instance = Message.objects.create()

                # check weather user has supplied a secret key or not
                if secret_key:
                    if not check_key_size_bytes(secret_key):
                        return HttpResponseBadRequest(errors.WRONG_AES_KEY_LENGTH.format(len(secret_key.encode('utf-8'))))
                    # encrypted message
                    encrypted_message = encode(message, secret_key)

                    instance.key = secret_key  # to validate the key for this message in future
                    instance.is_encrypted = True # yes, the message is encrypted
                    instance.message = encrypted_message # set the cipher text
                    instance.save()  # save
                else:
                    # if user has not provided the secret key, then the we save the message as it is.
                    instance.is_encrypted = False
                    instance.message = message  # in this case cipher text is equal to the message itself
                    instance.save()

                return HttpResponseRedirect(reverse('show-encrypted-message', args=(instance.pk,)))
            return render(request, self.template_name, {'form': form})
        except Exception as e:
            return HttpResponseBadRequest(errors.STANDARD_ERROR_TEMPLATE.format(e.args or e.message))


class ShowEncryptedMessage(View):
    """
    Shows the encrypted message and a button to add a secret key to decrypt the message
    """
    form_class = ReadMessageForm
    template_name = 'encrypted_message.html'
    initial = {}

    def get(self, request, *args, **kwargs):
        """
        :param request: HttpRequest object
        :param args: list of args
        :param kwargs: key words
        :return: a form which shows encrypted message and a space to enter a secret key which then decrypts the message
        """
        try:
            instance = Message.objects.get(pk=args[0])
            form = self.form_class()
            return render(request, self.template_name, {'form': form, 'message': instance.message})
        except Exception as e:
            return HttpResponseBadRequest(errors.STANDARD_ERROR_TEMPLATE.format(e.args or e.message))

    def post(self, request, *args, **kwargs):
        """
        :param request:
        :return: handles the decryption. Decrypts the message and outputs on a separate HTML page.
        """
        try:

            form = self.form_class(request.POST)
            instance = Message.objects.get(pk=args[0])

            if form.is_valid():

                secret_key = form.cleaned_data['secret_key']
                # check weather user has supplied a secret key or not
                if secret_key:
                    # check  the key sizes
                    if not check_key_size_bytes(secret_key):
                        return HttpResponseBadRequest(errors.WRONG_AES_KEY_LENGTH.format(len(secret_key.encode('utf-8'))))

                    # check that the key you provided matches with our stored key
                    if instance.key and (not (secret_key == instance.key)):
                        return HttpResponseBadRequest(errors.INVALID_KEY)

                    # if even after proving the key, the message is marked as not encrypted, we return the message
                    if not instance.is_encrypted:
                        return render(request, 'decrypted_message.html', {'message': instance.message})

                    # if the message is really encrypted, we decrypt it and return the message
                    decoded_string = decode(instance.message, instance.key)
                    return render(request, 'decrypted_message.html', {'message': decoded_string})

                # if you do not provide the key, and you are trying to decrypt the message, then we check if the message is really encrypted
                if not instance.is_encrypted:
                    return render(request, 'decrypted_message.html', {'message': instance.message})

                # if it is encrypted, then it's an error. You must provide the secret key
                return HttpResponseBadRequest('The message you are trying to decrypt requires a secret key. You must provide the secret key')

            return render(request, self.template_name, {'form': form})

        except Exception as e:
            return HttpResponseBadRequest(errors.STANDARD_ERROR_TEMPLATE.format(e.args or e.message))