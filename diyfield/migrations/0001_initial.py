# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import diyfield.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('labels', diyfield.models.ListField()),
            ],
        ),
    ]
