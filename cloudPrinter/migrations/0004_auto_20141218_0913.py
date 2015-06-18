# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloudPrinter', '0003_tasklist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasklist',
            name='filePath',
        ),
        migrations.AddField(
            model_name='tasklist',
            name='fileName',
            field=models.CharField(default=b'testPaper', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tasklist',
            name='fileType',
            field=models.CharField(default=b'typeTest', max_length=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tasklist',
            name='md5',
            field=models.CharField(default=b'testMD5', max_length=100),
            preserve_default=True,
        ),
    ]
