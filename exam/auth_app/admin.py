from django.contrib import admin

from exam.auth_app.models import Profile, AppUser

admin.site.register(AppUser)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')