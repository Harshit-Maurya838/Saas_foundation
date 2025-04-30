from django.urls import path
from .views import profile_detail_view, profile_list

urlpatterns = [
    path("", profile_list, name='profile_list'),
    path("<str:username>/", profile_detail_view, name='profile'),
]
