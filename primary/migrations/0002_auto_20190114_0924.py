# Generated by Django 2.2 on 2019-01-14 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementary',
            name='Elementary_Name',
            field=models.CharField(max_length=8),
        ),
    ]
