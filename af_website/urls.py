from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from account.views import *
from mysite import views
from account.templates import *
urlpatterns = [
    #account urls
    path('register/', registration_view, name = 'register'),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('application_status/', application_status_view, name = 'application status'),

    #passsword reset/change urls
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),

    #mysite urls
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.index, name='index1'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog_post/<int:pk>', views.blog_post, name='blog_post'),
    path('contact/', views.contact, name='contact'),
    path('udaan/', views.udaan_view, name='udaan'),
    path('gallery/', views.gallery, name='gallery'),
    path('events/', views.events, name='events'),
    path('team/', views.team, name = 'team'),
    path('udaan/thank_you', views.thank_you, name='thank_you'),
    path('volunteer_registration', volunteer_form_view, name='volunteer_registration')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)