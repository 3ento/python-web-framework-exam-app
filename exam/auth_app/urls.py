from django.urls import path
from exam.auth_app.views import UserLoginView, ProfileDelete, UserEdit
from exam.auth_app.views import ProfileDetails, ProfileCreate, ProfileEdit, ProfileLogOut

urlpatterns = (
    path('logout', ProfileLogOut.as_view(), name='profile_logout'),
    path('create/', ProfileCreate.as_view(), name='profile_create'),
    path('<int:pk>', ProfileDetails.as_view(), name='profile_details'),

    path('edit/<int:pk>', ProfileEdit.as_view(), name='profile_edit'),
    path('user/edit/<int:pk>', UserEdit.as_view(), name='profile_user_edit'),

    path('delete/<int:pk>', ProfileDelete.as_view(), name='delete profile'),
)