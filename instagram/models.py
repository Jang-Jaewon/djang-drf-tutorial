from django.db import models

from core.models import TimeStamp


class Post(TimeStamp):
    message = models.TextField()
    
