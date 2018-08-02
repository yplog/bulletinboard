from django.urls import path
from . import views


urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:bulletin_id>/up', views.up, name='up'),
]
