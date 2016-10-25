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
    # M2M Field를 사용해서 좋아요 내용을 거치도록 합니다 (중간자 모델)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='PhotoLike', related_name='photo_set_like_users')
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='PhotoDislike', related_name='photo_set_dislike_users')
# Many to many field에서 중간에 생성되는 table과 같다

class PhotoLike(models.Model):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)


class PhotoDislike(models.Model):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)