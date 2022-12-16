from django.urls import path
from exam.main.views.music_views import MusicCommentEdit, MusicCommentDelete

urlpatterns = [
    path('edit/<int:pk>', MusicCommentEdit.as_view(), name='edit comment'),
    path('delete/<int:pk>', MusicCommentDelete.as_view(), name='delete comment'),
]