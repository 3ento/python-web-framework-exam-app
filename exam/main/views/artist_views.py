from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import FormMixin, UpdateView, DeleteView

from exam.main.forms import CreateArtist
from exam.main.models import Artist, MusicCollections


class ArtistCreate(LoginRequiredMixin, CreateView):
    model = Artist
    form_class = CreateArtist
    template_name = 'main/artist/artist_create.html'

    success_url = reverse_lazy('dashboard artists')

class ArtistDetails(DetailView):
    model = Artist
    template_name = 'main/artist/artist_details.html'
    context_object_name = 'artist'

    def get_context_data(self, **kwargs):
        discography = MusicCollections.objects.filter(artist_id=self.object.id)

        follow = get_object_or_404(Artist, id=self.kwargs['pk'])
        followed = False
        if follow.followers.filter(id=self.request.user.id).exists():
            followed = True

        context = super().get_context_data(**kwargs)
        context.update({
            'music': discography,
            'genre': str(self.object.genres),
            'number_of_followers': follow.number_of_followers(),
            'artist_is_followed': followed,
            'current_user': self.request.user,
        })

        return context

class ArtistEdit(LoginRequiredMixin, UpdateView):
    model = Artist
    fields = ('name', 'picture', 'description', 'genres')
    template_name = 'main/artist/artist_edit.html'
    context_object_name = 'artist'

    def get_success_url(self):
        artist_id = self.kwargs['pk']
        return reverse_lazy('artist details', kwargs={'pk': artist_id})

class ArtistDelete(LoginRequiredMixin, DeleteView):
    model = Artist
    template_name = 'main/artist/artist_delete.html'
    success_url = reverse_lazy('dashboard artists')