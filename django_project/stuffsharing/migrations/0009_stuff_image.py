# Generated by Django 2.2 on 2019-04-07 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuffsharing', '0008_auto_20190407_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='stuff',
            name='image',
            field=models.CharField(default='', max_length=1000),
        ),
    ]