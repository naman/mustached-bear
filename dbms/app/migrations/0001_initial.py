# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_no', models.IntegerField(serialize=False, primary_key=True)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('zip', models.IntegerField(max_length=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_no', models.IntegerField(serialize=False, primary_key=True)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('zip', models.IntegerField(max_length=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_no', models.IntegerField(serialize=False, primary_key=True)),
                ('recv_date', models.DateTimeField()),
                ('ship_date', models.DateTimeField()),
                ('customer', models.ForeignKey(to='app.Customer')),
                ('employee', models.ForeignKey(to='app.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Order_Part_Quantity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('part_quantity', models.IntegerField()),
                ('order_no', models.ForeignKey(to='app.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('part_no', models.IntegerField(serialize=False, primary_key=True)),
                ('pname', models.CharField(max_length=20)),
                ('price', models.IntegerField(max_length=4)),
                ('max_quantity', models.IntegerField(max_length=4)),
            ],
        ),
        migrations.AddField(
            model_name='order_part_quantity',
            name='part_no',
            field=models.ForeignKey(to='app.Part'),
        ),
    ]
