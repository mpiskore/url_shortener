import random
import string

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class UrlMapper(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.CharField(max_length=512, unique=True)
    shortened_url = models.CharField(max_length=64)

    @classmethod
    def get_shortened_url(cls):
        char_pool = string.ascii_lowercase + string.ascii_uppercase + string.digits
        return "".join(
            [random.choice(char_pool) for _ in range(settings.SHORT_URL_MAX_LEN)]
        )
