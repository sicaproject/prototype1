# Generated by Django 3.1.1 on 2020-10-04 14:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0016_auto_20201004_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classsj',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 4, 19, 44, 48, 627558)),
        ),
    ]
