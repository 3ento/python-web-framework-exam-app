from django.contrib import admin
from django.contrib.auth.models import Group

from exam.main.models import MusicCollections, Artist, MusicTracks

# Register your models here.
admin.site.register(MusicCollections)
admin.site.register(Artist)
admin.site.register(MusicTracks)

admin.site.unregister(Group)