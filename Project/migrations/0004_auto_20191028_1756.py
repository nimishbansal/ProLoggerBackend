# Generated by Django 2.2.3 on 2019-10-28 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0003_project_secret_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logentry',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]