# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloudPrinter', '0004_auto_20141218_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='calledTime',
            field=models.DateTimeField(auto_now=True, auto_now_add=True),
            preserve_default=True,
        ),
    ]
