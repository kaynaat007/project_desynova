from django.db import models

# Create your models here.


class Url(models.Model):
    """
    Model that stores the input url and corresponding shorter url
    """
    input_url = models.URLField(max_length=100, unique=True)
    shorter_url = models.URLField(max_length=100, null=True, blank=True)
