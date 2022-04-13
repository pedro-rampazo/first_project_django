from django.urls import path
from user_data_viewer import views

urlpatterns = [
    path('', views.index, name='index'),
    path('persons/', views.PersonListView.as_view(), name='persons'),
]
