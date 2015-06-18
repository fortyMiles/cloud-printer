# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cloudPrinter', '0007_auto_20141223_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='calledTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 23, 16, 25, 24, 195663), auto_now=True, auto_now_add=True),
            preserve_default=True,
        ),
    ]
