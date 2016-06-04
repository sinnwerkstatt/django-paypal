# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0007_auto_20160219_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paypalpdt',
            name='notify_version',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
