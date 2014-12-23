# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='distance_to_bar',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
