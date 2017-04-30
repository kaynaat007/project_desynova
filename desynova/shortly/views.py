from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

from .forms import UrlForm
from .models import Url
from .utils import to_string


class UrlShortenerView(View):
    """
    View displays a form and let the user enter a url. when user submits the form, it redirects and
    display's a shorter version of the same url.
    """
    form_class = UrlForm
    template_name = 'basic.html'
    initial = {}

    def get(self, request, *args, **kwargs):
        """
        :param request: The Django HttpRequest object
        :param args: list of args
        :param kwargs: key word args
        :return: a HTML form.
        """

        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        """
        :param request: The Django HttpRequest object
        :param args: list of args
        :param kwargs: key words
        :return: redirects to a new HTML page if form data was processed successfully else returns the same form
        """
        form = self.form_class(request.POST)
        if form.is_valid():
            input_url = form.cleaned_data['input_url']
            instance, is_created = Url.objects.get_or_create(input_url=input_url)
            # create only if shorter_url field is not none.
            if not instance.shorter_url:
                instance.shorter_url = request.META['HTTP_ORIGIN'] + '/' + to_string(instance.pk)
                instance.save()
            return HttpResponseRedirect(reverse('show-short-url', args=(instance.pk,)))
        return render(request, self.template_name, {'form': form})


def show_shorten_url(request, url_id):
    """
     In order to show the new shorter url, there was no need of using a class based view. Hence wrote a simple function
     based view which does the job of displaying the shorter url and redirecting to original url
    :param request:
    :param url_id:
    :return:
    """
    try:
        instance = Url.objects.get(pk=url_id)
    except ObjectDoesNotExist as e:
        return HttpResponseBadRequest('The object with id {0} does not exist in the system'.format(url_id))
    return render(request, 'output.html', {'short_url': instance.shorter_url, 'original_url': instance.input_url})
