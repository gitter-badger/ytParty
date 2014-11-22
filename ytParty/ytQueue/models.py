from django.db import models
from embed_video.fields import EmbedVideoField


class Party(models.Model):
    host_id = models.ForeignKey(User)
    PARTY_STATUS = (
        ('P', 'Running'),
        ('R', 'Paused'),
    )
    status = models.CharField(choices=PARTY_STATUS)


class QueueRow(models.Model):
    video = EmbedVideoField()


class UserActivity(models.Model):
    party_id = models.ForeignKey(Party)


class User(models.Model):
