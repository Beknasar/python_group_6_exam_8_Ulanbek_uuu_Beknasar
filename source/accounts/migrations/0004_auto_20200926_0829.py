# Generated by Django 2.2 on 2020-09-26 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200926_0656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='about',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='link',
        ),
    ]
