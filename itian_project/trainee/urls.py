from django.urls import path
from .views import trainee_list, create_trainee, update_trainee, delete_trainee, trainee_details

urlpatterns = [
    path("", trainee_list, name="trainee_list"),
    path("create/", create_trainee, name="create_trainee"),
    path("update/<int:id>/", update_trainee, name="update_trainee"),
    path("delete/<int:id>/", delete_trainee, name="delete_trainee"),
    path("details/<int:id>/", trainee_details, name="trainee_details"),
]
