# Generated by Django 4.0.4 on 2022-04-21 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='filetype',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]