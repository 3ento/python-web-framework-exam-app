from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from exam.main.models import MusicCollections, Artist


def MusicSave(request, pk):
    post = get_object_or_404(MusicCollections, id=request.POST.get('blogpost_id'))
    if post.saves.filter(id=request.user.id).exists():
        post.saves.remove(request.user)
    else:
        post.saves.add(request.user)

    return HttpResponseRedirect(reverse('music details', args=[str(pk)]))

def ArtistFollow(request, pk):
    post = get_object_or_404(Artist, id=request.POST.get('blogpost_id'))
    if post.followers.filter(id=request.user.id).exists():
        post.followers.remove(request.user)
    else:
        post.followers.add(request.user)

    return HttpResponseRedirect(reverse('artist details', args=[str(pk)]))

class BootstrapFormMixin:
    fields = {}

    def _init_bootstrap_form_controls(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += ' form-control'