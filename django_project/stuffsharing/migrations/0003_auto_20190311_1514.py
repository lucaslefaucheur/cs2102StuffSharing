# Generated by Django 2.1.7 on 2019-03-11 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuffsharing', '0002_auto_20190311_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='stuff',
            name='tags',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='description',
            field=models.CharField(default='', max_length=255),
        ),
    ]
