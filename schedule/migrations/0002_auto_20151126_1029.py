# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name_plural': 'classes', 'ordering': ['start_date_time']},
        ),
        migrations.AlterField(
            model_name='class',
            name='location',
            field=models.ForeignKey(null=True, related_name='classes', to='schedule.Location'),
        ),
    ]
