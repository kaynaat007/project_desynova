from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'desynova.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^shortly/', include('shortly.urls')),
    url(r'^paste-lockly/', include('paste_lockly.urls')),

]
