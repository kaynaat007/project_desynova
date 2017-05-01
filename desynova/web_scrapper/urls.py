from django.conf.urls import url

from .views import GainerLooserView
urlpatterns = [
    url(r'^gainer-loser-data/$', GainerLooserView.as_view() , name='gainer-loser-data'),

]