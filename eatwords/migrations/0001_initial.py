# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EatwordsConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('user_id', models.CharField(max_length=100, default=0)),
                ('book_id', models.CharField(max_length=100, default=0)),
                ('count_id', models.CharField(max_length=100, default=0)),
                ('ok_id', models.CharField(max_length=100, default=0)),
                ('progress', models.CharField(max_length=100, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': '背单词配置',
                'db_table': 'eartwords_config',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='WordNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('user_id', models.CharField(max_length=100, default=0)),
                ('word_id', models.CharField(max_length=100, default=0)),
                ('note_content', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': '用户单词笔记',
                'db_table': 'word_note',
                'ordering': ['id'],
            },
        ),
    ]
