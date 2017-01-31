from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Event(models.Model):
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField()
    title = models.CharField(max_length=250)
    description = models.TextField()
    location = models.CharField(max_length=250)


class FeedEntry(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    timestamp = models.DateTimeField()


class Comment(models.Model):
    user = models.ForeignKey(User)
    feed_entry = models.ForeignKey(FeedEntry)
    timestamp = models.DateTimeField()
    text = models.TextField()


class Building(models.Model):
    user = models.ForeignKey(User)
    address = models.CharField(max_length=250)
    # building_owner = models.ForeignKey(User, null=True)


class Apartment(models.Model):
    building = models.ForeignKey(Building)
    floor = models.IntegerField()
    apartment_number = models.CharField(max_length=250)
    # apartment_owner = models.ForeignKey(User, null=True)


class Account(models.Model):
    user = models.ForeignKey(User)
    contact_number = models.CharField(max_length=250)
    manager = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)
