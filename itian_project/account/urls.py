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
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('accounts/', list_account, name='account_list'),
    path('accounts/Add/', create_account, name='account_create'),
    path('accounts/Update/<int:id>/', update_account, name='account_update'),
    path('accounts/Delete/<int:id>/', delete_account, name='account_delete'),
    path('accounts/Details/<int:id>/', account_details, name='account_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
