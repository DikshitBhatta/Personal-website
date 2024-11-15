from django.urls import path, include
from django.contrib import admin
import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL displays header as homepage
    path('admin-panel/', admin.site.urls),
    path('home/', views.homePage, name='home'),
    path('about/', views.About, name='about'),
    path('Experience/', views.Experience, name='Experience'),
    path('projects/', views.Projects, name='projects'),
]
  