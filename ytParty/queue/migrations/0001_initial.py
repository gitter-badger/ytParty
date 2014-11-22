# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=1, choices=[(b'P', b'Running'), (b'R', b'Paused')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserParties',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('party_id', models.ForeignKey(to='queue.Party')),
                ('user_id', models.ForeignKey(to='queue.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('votes', models.IntegerField()),
                ('time_added', models.DateTimeField(auto_now_add=True)),
                ('token', models.CharField(max_length=12)),
                ('status', models.CharField(max_length=1, choices=[(b'F', b'Finished'), (b'P', b'Playing'), (b'Q', b'Queued')])),
                ('party_id', models.ForeignKey(to='queue.Party')),
                ('user_id', models.ForeignKey(to='queue.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='party',
            name='host_id',
            field=models.ForeignKey(to='queue.User'),
            preserve_default=True,
        ),
    ]
