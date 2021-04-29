# Generated by Django 3.1.6 on 2021-02-28 05:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsAPI', '0004_auto_20210228_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsapi',
            name='save',
            field=models.ManyToManyField(blank=True, related_name='save_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Savenewsapi',
        ),
    ]