# Generated by Django 3.0.8 on 2020-09-27 16:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0009_auto_20200927_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='classwork',
            name='filess',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='classsj',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 27, 21, 50, 25, 713891)),
        ),
    ]
