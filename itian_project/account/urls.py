# from django.urls import path
# from .views import *
# from .import views
#
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('accounts/', list_account, name='account_list'),
#     path('accounts/Add/', create_account, name='account_create'),
#     path('accounts/Update/<int:id>/', update_account, name='account_update'),
#     path('accounts/Delete/<int:id>/', delete_account, name='account_delete'),
#     path('accounts/Details/<int:id>/', account_details, name='account_details'),
# ]

from django.urls import path
from .views import (
    index,
    list_account,
    create_account,
    update_account,
    delete_account,
    account_details,
)

urlpatterns = [
    path('', index, name='index'),
    path('accounts/', list_account, name='account_list'),
    path('accounts/Add/', create_account, name='account_create'),
    path('accounts/Update/<int:id>/', update_account, name='account_update'),
    path('accounts/Delete/<int:id>/', delete_account, name='account_delete'),
    path('accounts/Details/<int:id>/', account_details, name='account_details'),
]
