# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloudPrinter', '0002_auto_20141217_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filePath', models.CharField(max_length=200)),
                ('copyNum', models.IntegerField()),
                ('userEmail', models.CharField(max_length=100)),
                ('calledTime', models.DateField(auto_now=True, auto_now_add=True)),
                ('prority', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
