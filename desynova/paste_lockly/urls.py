from django.conf.urls import url

from views import MessageView, ShowEncryptedMessage

urlpatterns = [
    url(r'^message/$', MessageView.as_view(), name='message'),
    url(r'^encrypted-message/([0-9]+)/$', ShowEncryptedMessage.as_view(), name='show-encrypted-message'),
]