# Generated by Django 4.1.4 on 2022-12-20 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_delete_musictrackcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='musiccollections',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]