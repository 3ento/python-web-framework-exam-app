from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from exam.auth_app.forms import CreateProfileForm, EditProfileForm, UserEditForm
from exam.auth_app.models import Profile, AppUser
from exam.main.models import MusicCollections, Artist


class UserLoginView(LoginView):
    template_name = 'auth_app/login_page.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        else:
            return super().get_success_url()

class ProfileLogOut(LogoutView):
    next_page = reverse_lazy('home')

class ProfileCreate(CreateView):
    form_class = CreateProfileForm
    template_name = 'auth_app/profile_create.html'
    success_url = reverse_lazy('dashboard music')

    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)
        login(self.request, self.object)

        return result

class ProfileDetails(DetailView):
    model = Profile
    template_name = 'auth_app/profile_details.html'

    def get_context_data(self, **kwargs):

        following = Artist.objects.filter(followers=self.object.user)
        saved = sorted(MusicCollections.objects.filter(saves__username=self.object.user.username), key=lambda x: x.artist.name, reverse=False)

        context = super().get_context_data(**kwargs)
        context.update({
            'is_owner': self.object.user == self.request.user,
            'count': len(following),
            'saved_songs': saved,
            'followed_artists': following,
            'current_user': self.request.user
        })

        return context

class ProfileEdit(UpdateView):
    model = Profile
    template_name = 'auth_app/profile_edit.html'
    form_class = EditProfileForm


    def get_success_url(self):
        user_page_id = self.kwargs['pk']
        return reverse_lazy("profile_details", kwargs={'pk': user_page_id})

class ProfileDelete(DeleteView):
    model = AppUser
    success_url = reverse_lazy('home')
    template_name = "auth_app/profile_delete.html"

class UserEdit(UpdateView):
    model = AppUser
    template_name = 'auth_app/profile_user_edit.html'
    form_class = UserEditForm

    def get_success_url(self):
        user_page_id = self.kwargs['pk']
        return reverse_lazy("profile_details", kwargs={'pk': user_page_id})

