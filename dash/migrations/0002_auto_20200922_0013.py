# Generated by Django 3.0.8 on 2020-09-21 18:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dash', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='classs',
            new_name='classsm',
        ),
    ]
