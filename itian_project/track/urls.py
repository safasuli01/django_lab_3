from django.urls import path, include
from .views import track_list, create_track, update_track, delete_track, track_details

urlpatterns = [
    path("", track_list, name="track_list"),
    path("create/", create_track, name="create_track"),
    path("update/<int:id>/", update_track, name="update_track"),
    path("delete/<int:id>/", delete_track, name="delete_track"),
    path("details/<int:id>/", track_details, name="track_details"),
    path('', include('home.urls')),
]
