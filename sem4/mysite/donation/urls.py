from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('donations', views.donations, name='donation'),
    path('mydonations', views.mydonations, name='mydonations'),
    path('edit_mydonations', views.edit_mydonations, name='edit_mydonations'),
    path('update_mydonations', views.update_mydonations,name='update_mydonations'),
    path('add_donation',views.add_donation, name='add_donation'),
    path('requestinfo',views.requestinfo,name='requestinfo'),
]