from django.urls import path

from profiles import views

urlpatterns = [
    path('', views.index, name='profile_index'),
    path('<str:username>/', views.profile, name='profile'),
]
