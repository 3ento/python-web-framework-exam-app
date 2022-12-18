from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

from exam.main.models import MusicCollections, Artist


def GenreDashboard(request, genre):
    template_name = 'main/dashboards/genre_dashboard.html'

    context = {
        'music': MusicCollections.objects.filter(artist__genres=genre),
        'genre': MusicCollections.objects.filter(artist__genres=genre)[0].artist.genres
    }

    return render(request, template_name, context)

def ChartsDashboard(request, chart):
    template_name = 'main/dashboards/charts_dashboard.html'

    charts = {
        'most_saved_music': sorted(MusicCollections.objects.all(), key=lambda x: x.number_of_saves(), reverse=True),
        'most_followed_artist': sorted(Artist.objects.all(), key=lambda x: x.number_of_followers(), reverse=True),
    }

    context = {
        'objects': charts[chart],
        'chart_type': chart,
        'temp': [charts[chart][0]],
    }

    return render(request, template_name, context)

class MusicDashboard(LoginRequiredMixin, TemplateView):
    template_name = 'main/dashboards/music_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['music'] = sorted(MusicCollections.objects.all(), key=lambda x: x.get_artist_name(), reverse=False)

        return context

class ArtistDashboard(LoginRequiredMixin, TemplateView):
    template_name = 'main/dashboards/artist_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artist'] = sorted(Artist.objects.all(), key=lambda x: x.name, reverse=False)

        return context



