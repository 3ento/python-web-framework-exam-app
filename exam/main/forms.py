from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django import forms
from exam.main.models import MusicCollectionComment, Artist

UserModel = get_user_model()

class CreatePhotoComment(ModelForm):
    class Meta:
        model = MusicCollectionComment
        fields = ('body', 'rating')
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'cols': 57}),
        }

class CreateArtist(ModelForm):
    class Meta:
        model = Artist
        fields = ('name', 'description', 'genres', 'picture')