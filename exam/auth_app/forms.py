from exam.auth_app.models import Profile, AppUser
from exam.main.common.common import BootstrapFormMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CreateProfileForm(BootstrapFormMixin, UserCreationForm):
    first_name = forms.CharField(
        max_length=25,
    )

    last_name = forms.CharField(
        max_length=25,
        required=False,
    )

    profile_picture = forms.URLField(
        required=True,
    )

    description = forms.CharField(
        widget=forms.Textarea,
        required=False,
    )

    pronouns = forms.ChoiceField(
        choices=Profile.PRONOUNS,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            profile_picture=self.cleaned_data['profile_picture'],
            description=self.cleaned_data['description'],
            pronouns=self.cleaned_data['pronouns'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'profile_picture', 'description')

class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = ('profile_picture', 'pronouns', 'description', 'last_name', 'first_name')

class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()

class UserEditForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = AppUser
        fields = ('is_superuser', 'is_staff')
