# Generated by Django 3.1.6 on 2021-04-15 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsAPI', '0013_newsapi_favourite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsapi',
            old_name='category',
            new_name='url',
        ),
    ]
