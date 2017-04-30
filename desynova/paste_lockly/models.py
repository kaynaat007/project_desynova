from django.db import models

# Create your models here.


class Message(models.Model):
    """
    The table which stores each message and it's attributes
    """
    message = models.CharField(max_length=1000)
    key = models.CharField(max_length=254, null=True, blank=True)
    is_encrypted = models.BooleanField(default=False)
    cipher_text = models.TextField(max_length=4000, null=True, blank=True)

