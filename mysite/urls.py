from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

# app_name = 'mysite'
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('index/', views.index, name='index1'),
#     path('about/', views.about, name='about'),
#     path('blog/', views.blog, name='blog'),
#     path('blog_details/', views.blog_details, name='blog_details'),
#     path('contact/', views.contact, name='contact'),
#     path('udaan/', views.udaan_view, name='udaan')
# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
