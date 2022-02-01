from django.conf import settings
from django.db   import models

from core.models import TimeStamp


class Post(TimeStamp):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    
