# Generated by Django 2.1.7 on 2019-04-08 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuffsharing', '0018_auto_20190408_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, default=123, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_name',
            field=models.CharField(max_length=255),
        ),
    ]
