"""exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from exam.auth_app.views import UserLoginView
from exam.main.views.core_views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('artist/', include('exam.main.urls.artist_urls')),
    path('dashboard/', include('exam.main.urls.dashboard_urls')),
    path('music/', include('exam.main.urls.music_urls')),
    path('track/', include('exam.main.urls.track_urls')),
    path('comment/', include('exam.main.urls.comment_urls')),
    path('profile/', include('exam.auth_app.urls')),

    path('login/', UserLoginView.as_view(), name='login'),

]
