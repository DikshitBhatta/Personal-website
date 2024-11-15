from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
import views

urlpatterns = [
    path('', views.header, name='header'),  # Root URL displays header as homepage
    path('admin-panel/', admin.site.urls),
    path('home/', views.homePage, name='home'),
    path('about/', views.About, name='about'),
    path('Experience/', views.Experience, name='Experience'),
    path('projects/', views.Projects, name='projects'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  