# Generated by Django 3.1.6 on 2021-04-15 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsAPI', '0014_auto_20210415_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsapi',
            name='category',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
