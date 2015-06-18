# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloudPrinter', '0005_auto_20141218_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='printerCode',
            field=models.CharField(default=b'0x001', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='fileName',
            field=models.CharField(default=b'testPaper', max_length=1002),
            preserve_default=True,
        ),
    ]
