# Generated by Django 2.2.3 on 2019-08-17 19:06

from django.db import migrations
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0009_exceptionstacktrace'),
    ]

    operations = [
        migrations.AddField(
            model_name='logentry',
            name='tags',
            field=django_mysql.models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
