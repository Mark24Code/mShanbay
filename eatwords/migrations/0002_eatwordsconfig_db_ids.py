# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eatwords', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eatwordsconfig',
            name='db_ids',
            field=models.TextField(blank=True, null=True),
        ),
    ]
