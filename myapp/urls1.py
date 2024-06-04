from django.urls import path
from myapp import views1

app_name = 'myapp'

urlpatterns = [
    path(r'', views1.index, name='index'),
    ]
