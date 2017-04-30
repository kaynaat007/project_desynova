# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortly', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='shorter_url',
            field=models.URLField(max_length=100, null=True, blank=True),
        ),
    ]
