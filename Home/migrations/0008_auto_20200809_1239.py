# Generated by Django 3.0.8 on 2020-08-09 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_auto_20200809_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='Phone',
            field=models.IntegerField(max_length=30),
        ),
    ]
