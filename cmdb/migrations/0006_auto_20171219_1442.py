# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-19 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0005_auto_20171216_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='status',
            field=models.SmallIntegerField(choices=[(1, '上线'), (2, '下线')], default=0, verbose_name='设备状态'),
        ),
        migrations.AlterField(
            model_name='server',
            name='lan_ip',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='内网IP'),
        ),
    ]