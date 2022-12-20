from django.db import models
from exam.auth_app.models import AppUser

class Artist(models.Model):
    GENRES = [
        ("Pop", "Pop"),
        ("Blues", "Blues"),
        ("Classical", "Classical"),
        ("Country", "Country"),
        ("Electronic", "Electronic"),
        ("Hip-hop", "Hip-hop"),
        ("Jazz", "Jazz"),
        ("Rock", "Rock"),
        ("Metal", "Metal"),
    ]

    name = models.CharField(
        max_length=50,
        unique=True,
    )


    fan_count = models.IntegerField(
        default=0,
    )

    picture = models.URLField()

    description = models.TextField(
        max_length=500,
    )

    genres = models.CharField(
        max_length=20,
        choices=GENRES,
    )

    followers = models.ManyToManyField(
        AppUser,
    )

    def show_more_description(self):
        return self.description[100:]

    def number_of_followers(self):
        return self.followers.count()

    def __str__(self):
        return self.name

class MusicCollections(models.Model):
    TYPES = [
        ("EP", "EP"),
        ("Album", "Album"),
        ("Mixtape", "Mixtape"),
        ("Single", "Single"),
    ]

    link = models.URLField()

    title = models.CharField(
        max_length=50,
        unique=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    added_at = models.DateTimeField(
        auto_now_add=True,
    )

    saves = models.ManyToManyField(
        AppUser,
        related_name='save_song'
    )

    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
    )

    type = models.CharField(
        max_length=20,
        choices=TYPES,
        default="",
    )

    def get_artist_name(self):
        return self.artist.name

    def show_more_description(self):
        return self.description[100:]

    def number_of_saves(self):
        return self.saves.count()

    def __str__(self):
        return self.title

class MusicTracks(models.Model):
    link = models.URLField()

    title = models.CharField(
        max_length=50,
    )

    lyrics = models.TextField(
        null=True,
        blank=True,
    )

    added_at = models.DateTimeField(
        auto_now_add=True,
    )

    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
    )

    collection = models.ForeignKey(
        MusicCollections,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

class MusicCollectionComment(models.Model):
    RATING_VALUES = ((i, i) for i in range(1, 11))

    body = models.TextField()

    rating = models.IntegerField(
        choices=RATING_VALUES,
        default=5,
    )

    post = models.ForeignKey(
        MusicCollections,
        on_delete=models.CASCADE,
    )

    added_at = models.DateTimeField(
        auto_now_add=True,
    )

    user = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        default='',
    )

