from django import forms


class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    secret_key = forms.CharField(max_length=254, help_text='optional secret key to encrypt the message', required=False)


class ReadMessageForm(forms.Form):
    secret_key = forms.CharField(max_length=254, help_text='optional secret key to decrypt the message', required=False)


