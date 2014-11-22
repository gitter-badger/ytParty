# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('queue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='token',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
