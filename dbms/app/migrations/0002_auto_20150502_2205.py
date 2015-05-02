# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('part_quantity', models.IntegerField()),
                ('order_no', models.ForeignKey(to='app.Order')),
                ('part_no', models.ForeignKey(to='app.Part')),
            ],
        ),
        migrations.RemoveField(
            model_name='order_part_quantity',
            name='order_no',
        ),
        migrations.RemoveField(
            model_name='order_part_quantity',
            name='part_no',
        ),
        migrations.DeleteModel(
            name='Order_Part_Quantity',
        ),
    ]
