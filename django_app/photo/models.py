from django.db import models
from django.conf import settings
# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=30)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = models.CharField(max_length=400, blank=True)
        # description은 required field가 아니므로 blank = True
class Photo(models.Model):
    Album = models.ForeignKey(Album)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=400, blank=True)
    img = models.ImageField(upload_to='photo')