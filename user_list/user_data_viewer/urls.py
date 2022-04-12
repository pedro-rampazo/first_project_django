from django.urls import path
from user_data_viewer import views

urlpatterns = [
    path('', views.index, name='index'),
]
