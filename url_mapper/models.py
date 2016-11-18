from django.contrib.auth.models import User
from django.db import models


class UrlMapper(models.Model):
    user = models.ForeignKey(User)
    original_url = models.CharField(max_length=512)
    shortened_url = models.CharField(max_length=64)
