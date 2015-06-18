# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cloudPrinter', '0010_auto_20141223_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='calledTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 24, 11, 41, 25, 776145), auto_now=True, auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='server_time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 24, 11, 41, 25, 776221)),
            preserve_default=True,
        ),
    ]
