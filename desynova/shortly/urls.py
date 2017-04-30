# urls.py
from django.conf.urls import url
from views import UrlShortenerView, show_shorten_url

urlpatterns = [
    url(r'^url-shortener/$', UrlShortenerView.as_view(), name='url-shortener'),
    url(r'^show-short-url/([0-9]+)/$', show_shorten_url, name='show-short-url'),

]