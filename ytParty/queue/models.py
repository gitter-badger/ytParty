from django.db import models
from django.contrib import admin


class User(models.Model):
    name = models.CharField(max_length=16, null=True)

    def __unicode__(self):
        return "pk: " + str(self.pk) + " name: " + str(self.name)


class Party(models.Model):
    host_id = models.ForeignKey(User)
    token = models.CharField(max_length=10, primary_key=True)
    PARTY_STATUS = (
        ('R', 'Running'),
        ('P', 'Paused'),
    )
    status = models.CharField(max_length=1, choices=PARTY_STATUS)

    def __unicode__(self):
        return str(self.token)


class Video(models.Model):
    party_id = models.ForeignKey(Party)
    votes = models.IntegerField(default=0)
    time_added = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=12)
    user_id = models.ForeignKey(User)
    VIDEO_STATUS = (
        ('F', 'Finished'),
        ('P', 'Playing'),
        ('Q', 'Queued'),
    )
    status = models.CharField(max_length=1, choices=VIDEO_STATUS, default='Q')

    def __unicode__(self):
        return str(self.token) + " " + str(self.party_id) + " " + self.status;


class UserParty(models.Model):
    user_id = models.ForeignKey(User)
    party_id = models.ForeignKey(Party)


class UserVote(models.Model):
    user = models.ForeignKey(User)
    video = models.ForeignKey(Video)
    delta = models.IntegerField()


admin.site.register(User)
admin.site.register(Party)
admin.site.register(Video)
admin.site.register(UserParty)
admin.site.register(UserVote)
