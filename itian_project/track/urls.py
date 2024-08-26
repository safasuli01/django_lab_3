from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", track_list, name="track_list"),
    path("create/", create_track, name="create_track"),
    path("update/<int:id>/", update_track, name="update_track"),
    path("delete/<int:id>/", delete_track, name="delete_track"),
    path("details/<int:id>/", track_details, name="track_details"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
