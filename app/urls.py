from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.create_new_user, name='register'),
    path('profile/', views.profile_view, name="profile"),
]
