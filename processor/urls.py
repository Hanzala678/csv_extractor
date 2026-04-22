from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload'),
    path('history/', views.history, name='history'),
]