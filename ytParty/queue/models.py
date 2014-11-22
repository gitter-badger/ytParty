from django.db import models


class User(models.Model):
    name = models.CharField(max_length=16)


class Party(models.Model):
    host_id = models.ForeignKey(User)
    token = models.CharField(max_length=5)
    PARTY_STATUS = (
        ('P', 'Running'),
        ('R', 'Paused'),
    )
    status = models.CharField(max_length=1, choices=PARTY_STATUS)


class Video(models.Model):
    party_id = models.ForeignKey(Party)
    votes = models.IntegerField()
    time_added = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=12)
    user_id = models.ForeignKey(User)
    VIDEO_STATUS = (
        ('F', 'Finished'),
        ('P', 'Playing'),
        ('Q', 'Queued'),
    )
    status = models.CharField(max_length=1, choices=VIDEO_STATUS)


class UserParties(models.Model):
    user_id = models.ForeignKey(User)
    party_id = models.ForeignKey(Party)
