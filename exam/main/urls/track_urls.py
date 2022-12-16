from django.urls import path
from exam.main.views.track_views import AddTrack, DetailsTrack, EditTrack, DeleteTrack

urlpatterns = [
    path('add/<int:id>', AddTrack.as_view(), name='create a track'),
    path('details/<int:pk>', DetailsTrack.as_view(), name='track details'),
    path('edit/<int:pk>', EditTrack.as_view(), name='track edit'),
    path('delete/<int:pk>', DeleteTrack.as_view(), name='track delete'),
]