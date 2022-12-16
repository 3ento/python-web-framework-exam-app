from django.urls import path
from exam.main.common.common import ArtistFollow
from exam.main.views.artist_views import ArtistCreate, ArtistDetails, ArtistEdit, ArtistDelete

urlpatterns = [
    path('create', ArtistCreate.as_view(), name='artist create'),
    path('edit/<int:pk>', ArtistEdit.as_view(), name='artist edit'),
    path('details/<int:pk>', ArtistDetails.as_view(), name='artist details'),
    path('delete/<int:pk>', ArtistDelete.as_view(), name='artist delete'),
    path('follow/<int:pk>', ArtistFollow, name='artist follow'),
]