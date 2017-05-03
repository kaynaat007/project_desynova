from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'desynova.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^shortly/', include('shortly.urls')),
    url(r'^paste-lockly/', include('paste_lockly.urls')),
    url(r'^web-scrapper/', include('web_scrapper.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
