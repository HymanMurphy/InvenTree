# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-16 12:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0019_auto_20180416_1249'),
        ('stock', '0008_stockitem_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockitem',
            name='batch',
            field=models.CharField(blank=True, help_text='Batch code for this stock item', max_length=100),
        ),
        migrations.AlterField(
            model_name='stockitem',
            name='belongs_to',
            field=models.ForeignKey(blank=True, help_text='Is this item installed in another item?', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='owned_parts', to='stock.StockItem'),
        ),
        migrations.AlterField(
            model_name='stockitem',
            name='customer',
            field=models.ForeignKey(blank=True, help_text='Item assigned to customer?', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stockitems', to='supplier.Customer'),
        ),
        migrations.AlterField(
            model_name='stockitem',
            name='location',
            field=models.ForeignKey(blank=True, help_text='Where is this stock item located?', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='items', to='stock.StockLocation'),
        ),
        migrations.AlterField(
            model_name='stockitem',
            name='serial',
            field=models.PositiveIntegerField(blank=True, help_text='Serial number for this item', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='stockitem',
            unique_together=set([('part', 'serial')]),
        ),
    ]