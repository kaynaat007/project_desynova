from django.conf.urls import url

from .views import GainerLooserView, DisplayPage
urlpatterns = [
    url(r'^gainer-loser-data/$', GainerLooserView.as_view() , name='gainer-loser-data'),
    url(r'^$', DisplayPage.as_view(), name='display-page'),

]