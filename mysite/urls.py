from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'mysite'
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index1'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog_post/<int:pk>', views.blog_post, name='blog_post'),
    path('contact/', views.contact, name='contact'),
    path('udaan/', views.udaan, name='udaan'),
    path('gallery/', views.gallery, name='gallery'),
    path('events/', views.events, name='events')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
