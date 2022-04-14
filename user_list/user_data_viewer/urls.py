from django.urls import path
from user_data_viewer import views

urlpatterns = [
    path('', views.index, name='index'),
    path('person/', views.PersonListView.as_view(), name='person'),
    path('person/<int:pk>', views.PersonDetailView.as_view(), name='person-detail'),
]
