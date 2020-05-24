from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'mysite'
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index1'),
]
