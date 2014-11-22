from django.db import models


class User(models.Model):
    name = models.CharField(max_length=16)


class Party(models.Model):
    host_id = models.ForeignKey(User)
    PARTY_STATUS = (
        ('P', 'Running'),
        ('R', 'Paused'),
    )
    status = models.CharField(max_length=1, choices=PARTY_STATUS)


class QueueRow(models.Model):
    pass


class UserParties(models.Model):
    user_id = models.ForeignKey(User)
    party_id = models.ForeignKey(Party)
