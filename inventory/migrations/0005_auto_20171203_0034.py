# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-03 00:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import inventory.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20171203_0018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fill',
            fields=[
                ('created', inventory.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', inventory.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batch', to='inventory.Batch')),
            ],
            options={
                'verbose_name': 'keg fill',
                'verbose_name_plural': 'keg fills',
                'ordering': ('created',),
            },
        ),
        migrations.RemoveField(
            model_name='keg',
            name='batch',
        ),
        migrations.AddField(
            model_name='fill',
            name='keg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keg', to='inventory.Keg'),
        ),
    ]