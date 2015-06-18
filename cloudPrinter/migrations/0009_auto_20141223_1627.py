# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cloudPrinter', '0008_auto_20141223_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='calledTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 23, 16, 27, 50, 29349), auto_now=True, auto_now_add=True),
            preserve_default=True,
        ),
    ]
