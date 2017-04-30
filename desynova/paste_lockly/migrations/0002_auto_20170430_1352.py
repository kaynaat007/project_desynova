# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paste_lockly', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='cipher_text',
            field=models.TextField(max_length=4000, null=True, blank=True),
        ),
    ]
