# Generated by Django 2.1.7 on 2019-04-05 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stuffsharing', '0005_auto_20190405_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanproposition',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='stuffsharing.Profile'),
        ),
    ]