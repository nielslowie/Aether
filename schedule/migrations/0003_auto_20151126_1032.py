# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('schedule', '0002_auto_20151126_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='location',
            field=models.ForeignKey(to='schedule.Location', null=True),
        ),
    ]
