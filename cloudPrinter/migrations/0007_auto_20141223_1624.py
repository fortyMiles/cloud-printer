# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cloudPrinter', '0006_auto_20141219_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasklist',
            name='printerCode',
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='calledTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 23, 16, 24, 10, 53467), auto_now=True, auto_now_add=True),
            preserve_default=True,
        ),
    ]
