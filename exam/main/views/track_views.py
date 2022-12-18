from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from exam.main.models import MusicTracks, MusicCollections


class AddTrack(LoginRequiredMixin, CreateView):
    model = MusicTracks
    template_name = 'main/music/tracks/track_add.html'
    fields = ('title', 'lyrics')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collection_id'] = self.kwargs['id']

        return context

    def get_success_url(self):
        music_post_id = self.kwargs['id']
        return reverse_lazy('music details', kwargs={'pk': music_post_id})

    def form_valid(self, form):
        music = MusicCollections.objects.get(pk=self.kwargs['id'])
        music_artist = MusicCollections.objects.get(pk=self.kwargs['id']).artist

        form.instance.link = music.link
        form.instance.artist = music_artist
        form.instance.collection_id = music.id

        return super().form_valid(form)

class DetailsTrack(LoginRequiredMixin, DetailView):
    model = MusicTracks
    template_name = 'main/music/tracks/track_details.html'
    context_object_name = 'track'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['current_user'] = self.request.user

        return ctx

class EditTrack(LoginRequiredMixin, UpdateView):
    model = MusicTracks
    template_name = 'main/music/tracks/track_edit.html'
    fields = ('link', 'title', 'lyrics')

    def get_success_url(self):
        track_id = self.kwargs['pk']
        return reverse_lazy('track details', kwargs={'pk': track_id})

class DeleteTrack(LoginRequiredMixin, DeleteView):
    model = MusicTracks
    template_name = 'main/music/tracks/track_delete.html'

    def get_success_url(self):
        artist_id = self.object.collection.id
        return reverse_lazy('music details', kwargs={'pk': artist_id})