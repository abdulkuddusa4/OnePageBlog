# Generated by Django 3.1.3 on 2020-11-17 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20201117_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
