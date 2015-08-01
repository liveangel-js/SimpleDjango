# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('bookid', models.AutoField(serialize=False, primary_key=True)),
                ('booklist', models.ForeignKey(to='blog.BlogPost')),
            ],
        ),
    ]
