# Generated by Django 4.0.2 on 2022-12-08 22:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_rename_description_musictracks_lyrics_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='followers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
    ]
