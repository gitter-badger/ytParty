from django.db import models
from embed_video.fields import EmbedVideoField


class User(models.Model):
    id = models.IntegerField(primary_key=True)


class Party(models.Model):
    host_id = models.ForeignKey(User)
    PARTY_STATUS = (
        ('P', 'Running'),
        ('R', 'Paused'),
    )
    status = models.CharField(max_length=1, choices=PARTY_STATUS)


class QueueRow(models.Model):
    video = EmbedVideoField()


class UserActivity(models.Model):
    user_id = models.ForeignKey(User)
    party_id = models.ForeignKey(Party)
