# Generated by Django 3.0.5 on 2020-04-26 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20200425_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coldentry',
            name='removed_packets',
            field=models.CharField(default='0', max_length=2000),
        ),
    ]
