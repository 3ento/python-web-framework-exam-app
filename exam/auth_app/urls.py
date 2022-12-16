from django.urls import path
from exam.auth_app.views import UserLoginView, ProfileDelete, UserEdit
from exam.auth_app.views import ProfileDetails, ProfileCreate, ProfileEdit, ProfileLogOut

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/logout', ProfileLogOut.as_view(), name='profile_logout'),
    path('profile/create/', ProfileCreate.as_view(), name='profile_create'),
    path('profile/<int:pk>', ProfileDetails.as_view(), name='profile_details'),

    path('profile/edit/<int:pk>', ProfileEdit.as_view(), name='profile_edit'),
    path('profile_user/edit/<int:pk>', UserEdit.as_view(), name='profile_user_edit'),

    path('profile/delete/<int:pk>', ProfileDelete.as_view(), name='delete profile'),
)