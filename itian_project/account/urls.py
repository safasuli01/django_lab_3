from django.urls import path
from .views import *

urlpatterns = [
    path("", list_account, name="account_list"),
    path("Add/", create_account, name="account_create"),
    path("Update/<int:id>", update_account, name="account_update"),
    path("Delete/<int:id>", delete_account, name="account_delete"),
    path("Details/<int:id>", account_details, name="account_details"),
]
