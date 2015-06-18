# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fileName', models.CharField(max_length=200)),
                ('fileType', models.CharField(max_length=200)),
                ('MD5', models.CharField(max_length=200)),
                ('lastPrintedDate', models.DateField()),
                ('printedTimes', models.IntegerField()),
                ('fileSavedPath', models.CharField(max_length=200)),
                ('fileSize', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
