from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from exam.main.forms import CreatePhotoComment
from exam.main.models import MusicCollections, MusicCollectionComment, MusicTracks, Artist


class MusicDetails(DetailView, FormMixin):
    model = MusicCollections
    form_class = CreatePhotoComment
    template_name = 'main/music/music_details.html'

    context_object_name = 'music'

    def get_success_url(self):
        return reverse('music details', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        comments = MusicCollectionComment.objects.filter(post_id=self.object.id)
        tracks = MusicTracks.objects.filter(collection=self.object)

        context['owner_name'] = self.object.artist
        context['owner_id'] = self.object.artist.id
        context['form'] = CreatePhotoComment(initial={'post': self.object})
        context['comments'] = comments
        context['tracks'] = tracks
        context['current_user'] = self.request.user
        if comments:
            context['rating'] = round(sum([int(el.rating) for el in comments]) / len(comments), 2)
        else:
            context['rating'] = 0

        likes_connected = get_object_or_404(MusicCollections, id=self.kwargs['pk'])
        liked = False
        if likes_connected.saves.filter(id=self.request.user.id).exists():
            liked = True
        context['number_of_likes'] = likes_connected.number_of_saves()
        context['post_is_liked'] = liked

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.object.id
        form.save()
        return super(MusicDetails, self).form_valid(form)

class MusicCreate(LoginRequiredMixin, CreateView):
    model = MusicCollections
    template_name = 'main/music/music_add.html'
    fields = ('title', 'description', 'link', 'artist', 'type')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('dashboard music')

class MusicCreateArtistSpecific(LoginRequiredMixin, CreateView):
    model = MusicCollections
    template_name = 'main/music/music_add_artist_specific.html'
    fields = ('title', 'description', 'link', 'type')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['artist_id'] = self.kwargs['pk']

        return context


    def get_success_url(self):
        music_post_id = self.kwargs['pk']
        return reverse_lazy('artist details', kwargs={'pk': music_post_id})

    def form_valid(self, form):
        artist_id = self.kwargs['pk']

        form.instance.user = self.request.user
        form.instance.artist = Artist.objects.get(pk=artist_id)
        return super().form_valid(form)

class MusicEdit(LoginRequiredMixin, UpdateView):
    model = MusicCollections
    fields = ('link', 'title', 'description', 'artist', 'type')
    template_name = 'main/music/music_edit.html'

    def get_success_url(self):
        music_post_id = self.kwargs['pk']
        return reverse_lazy('music details', kwargs={'pk': music_post_id})

class MusicDelete(LoginRequiredMixin, DeleteView):
    model = MusicCollections
    template_name = 'main/music/music_delete.html'

    success_url = reverse_lazy('dashboard music')

class MusicCommentEdit(LoginRequiredMixin, UpdateView):
    model = MusicCollectionComment
    fields = ('body', 'rating')
    template_name = 'main/music/comment/music_comment_edit.html'

    def get_success_url(self):
        original_post = MusicCollectionComment.objects.get(id=self.kwargs['pk']).post_id

        return reverse_lazy('music details', kwargs={'pk': original_post})

class MusicCommentDelete(LoginRequiredMixin, DeleteView):
    model = MusicCollectionComment
    template_name = 'main/music/comment/music_comment_delete.html'

    def get_success_url(self):
        original_post = MusicCollectionComment.objects.get(id=self.kwargs['pk']).post_id

        return reverse_lazy('music details', kwargs={'pk': original_post})