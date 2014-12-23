# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('proximity_to_volcanoe', models.IntegerField()),
                ('school_rating', models.IntegerField()),
                ('distance_to_bar', models.IntegerField()),
                ('image', models.URLField()),
                ('home_type', models.CharField(max_length=100)),
                ('distance_to_public_transit', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num_bedrooms', models.IntegerField()),
                ('num_bathrooms', models.IntegerField()),
                ('sq_ft', models.IntegerField()),
                ('lot_sq_ft', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='property',
            name='size',
            field=models.ForeignKey(to='Home.Size'),
            preserve_default=True,
        ),
    ]
