from django.db import models
from django.contrib.auth.models import User
from social_auth.fields import JSONField


class UserDetail(models.Model):
    user = models.OneToOneField(User)
    user_name = models.TextField()
    uid = models.CharField(max_length=20)
    head_img = models.URLField(max_length=100)
    want_say = models.CharField(max_length=9999)
    position = models.TextField(blank=True, null=True)
    extra = JSONField(default='{}')

    def __unicode__(self):
        return self.user_name

from django.db.models.signals import post_save


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserDetail.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
