from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    # path("", trainee_list, name="trainee_list"),
    # path("Add/", create_trainee, name="create_trainee"),
    # path("update/<int:id>/", update_trainee, name="update_trainee"),
    # path("delete/<int:id>/", delete_trainee, name="delete_trainee"),
    # path("details/<int:id>/", trainee_details, name="trainee_details"),
    path("", TraineeList.as_view(), name="trainee_list"),
    path("Add/", CreateTrainee.as_view(), name="create_trainee"),
    path("Update/<int:id>", update_trainee(), name="update_trainee"),
    path("Delete/<int:id>", delete_trainee(), name="delete_trainee"),
    path("Details/<int:id>", trainee_details, name="trainee_details"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)