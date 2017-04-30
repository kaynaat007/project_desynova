from django import forms


class UrlForm(forms.Form):
    input_url = forms.URLField(label='Enter URL', max_length=100)