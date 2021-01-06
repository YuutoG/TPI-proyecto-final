from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from users import views
from django.urls import path


urlpatterns = [
    # Sección para usuarios
    path('', views.pagina),
    path('inicio/', views.inicio),
    path('signup/', views.signup, name='signup'),
    path('login', views.login),
    path('logout/', views.logout),
    path('profile/', views.profile, name='profile'),
    path('upload/', views.loadPicture, name='upload'),
    path('admin/', admin.site.urls),
    url(r'^reset/password_reset', password_reset, 
        {'template_name':'registration/password_reset_form.html',
        'email_template_name': 'registration/password_reset_email.html'}, 
        name='password_reset'), 
    url(r'^password_reset_done', password_reset_done, 
        {'template_name': 'registration/password_reset_done.html'}, 
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, 
        {'template_name': 'registration/password_reset_confirm.html'},
        name='password_reset_confirm'
        ),
    url(r'^reset/done', password_reset_complete, {'template_name': 'registration/password_reset_complete.html'},
        name='password_reset_complete'),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

