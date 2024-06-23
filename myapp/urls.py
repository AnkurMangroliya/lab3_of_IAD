from django.urls import path, include
from . import views
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'myapp'

urlpatterns = [
    # path('', views.home, name='home'),
    path(r'', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('home.html', views.home, name='home_html'),
    path('about.html', views.about, name='about_html'),
    path('<int:book_id>/', views.detail, name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
