# Generated by Django 3.1.13 on 2021-09-25 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldworker',
            name='first_name',
            field=models.CharField(default='sandro', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fieldworker',
            name='last_name',
            field=models.CharField(default='sandro', max_length=255),
            preserve_default=False,
        ),
    ]