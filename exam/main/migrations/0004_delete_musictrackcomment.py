# Generated by Django 4.1.4 on 2022-12-17 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_artist_followers_delete_follow'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MusicTrackComment',
        ),
    ]