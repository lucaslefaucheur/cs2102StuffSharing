# Generated by Django 2.1.7 on 2019-04-08 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuffsharing', '0009_stuff_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adress',
            name='adress_name',
            field=models.CharField(default='', max_length=255, primary_key=True, serialize=False),
        ),
    ]
