# Generated by Django 2.1.7 on 2019-04-10 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stuffsharing', '0005_auto_20190409_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loanproposition',
            name='bid',
        ),
    ]