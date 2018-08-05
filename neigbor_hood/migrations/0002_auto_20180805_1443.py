# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-05 14:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neigbor_hood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='neighbor_hood',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='business',
            name='neighbor_hood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hoodbus', to='neigbor_hood.Neighbor_hood'),
        ),
        migrations.AddField(
            model_name='business',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business', to=settings.AUTH_USER_MODEL),
        ),
    ]
