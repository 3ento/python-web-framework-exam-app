from django.urls import path
from exam.main.views.music_views import MusicDetails, MusicCreate, MusicEdit, MusicDelete, MusicCreateArtistSpecific
from exam.main.common.common import MusicSave

urlpatterns = [
    path('details/<int:pk>', MusicDetails.as_view(), name='music details'),
    path('create/', MusicCreate.as_view(), name='music add'),
    path('create/<int:pk>', MusicCreateArtistSpecific.as_view(), name='music add artist specific'),
    path('edit/<int:pk>', MusicEdit.as_view(), name='music edit'),
    path('delete/<int:pk>', MusicDelete.as_view(), name='music delete'),
    path('save/<int:pk>', MusicSave, name='save a song'),
]