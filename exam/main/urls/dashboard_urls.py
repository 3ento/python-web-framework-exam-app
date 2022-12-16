from django.urls import path
from exam.main.views.dashboard_views import MusicDashboard, ArtistDashboard, GenreDashboard, ChartsDashboard

urlpatterns = [
    path('music', MusicDashboard.as_view(), name='dashboard music'),
    path('artists', ArtistDashboard.as_view(), name='dashboard artists'),
    path('genre/<str:genre>', GenreDashboard, name='dashboard genre'),
    path('charts/<str:chart>', ChartsDashboard, name='dashboard charts'),
]