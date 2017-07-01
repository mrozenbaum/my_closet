from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    """
    purpose: Creates Category table within database
        Example useage:

    args: models.Model: (NA): models class given by Django

    returns: (None): N/A
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_name = models.CharField(blank=True, null=False, max_length=35)
    birth_date = models.DateField(blank=True, null=False, max_length=10)
    zip_code = models.CharField(blank=True, null=False, max_length=10)
    bio = models.CharField(blank=True, null=False, max_length=150)

    def __str__(self):  # __unicode__ on Python 2
        return self.user.first_name

    # listen for changes on user. update post-save
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    # listen for changes on user. update post-save
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
