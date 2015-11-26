# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('start_date_time', models.DateTimeField()),
                ('end_date_time', models.DateTimeField()),
                ('activity', models.CharField(blank=True, max_length=64)),
                ('topic', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['start_date_time'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=64)),
                ('street', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('country', models.CharField(max_length=64, default='Belgium')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('courses', models.ManyToManyField(to='schedule.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='course',
            field=models.ForeignKey(to='schedule.Course'),
        ),
        migrations.AddField(
            model_name='class',
            name='location',
            field=models.ForeignKey(to='schedule.Location', null=True),
        ),
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.ForeignKey(to='schedule.Teacher', null=True),
        ),
    ]
