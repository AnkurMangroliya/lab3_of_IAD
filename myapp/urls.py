from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('home.html', views.home, name='home_html'),
    path('about.html', views.about, name='about_html'),
]
