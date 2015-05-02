# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='zip',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='zip',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='part',
            name='max_quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='part',
            name='price',
            field=models.IntegerField(),
        ),
    ]
