from django.urls import path, include
<<<<<<< HEAD
=======
from . import views
>>>>>>> ce204b837a20845cd59a0f8bbd40be31aa47f5fc
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
<<<<<<< HEAD
    path('<int:book_id>/', views.detail, name='detail'),
    path('feedback/', views.getFeedback, name='feedback1'),
    path('findbooks/', views.findbooks, name='findbooks'),
=======

>>>>>>> ce204b837a20845cd59a0f8bbd40be31aa47f5fc
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
