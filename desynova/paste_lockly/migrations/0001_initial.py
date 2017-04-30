# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=1000)),
                ('key', models.CharField(max_length=254, null=True, blank=True)),
                ('is_encrypted', models.BooleanField(default=False)),
                ('cipher_text', models.TextField(null=True, blank=True)),
            ],
        ),
    ]
