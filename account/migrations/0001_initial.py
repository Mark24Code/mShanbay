# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(null=True, auto_created=True)),
                ('user_id', models.CharField(default=0, max_length=100)),
                ('nickname', models.CharField(null=True, max_length=64)),
                ('avatar', models.URLField(default='/static/img/default_avatar.jpg')),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'user_profile',
                'verbose_name': '用户资料',
            },
        ),
    ]
