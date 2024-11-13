from django.urls import path, include
from django.contrib import admin
from travello import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL displays header as homepage
    path('admin-panel/', admin.site.urls),
    path('home/', views.homePage, name='home'),
    path('about/', views.About, name='about'),
    path('experience/', views.Experience, name='experience'),
    path('projects/', views.Projects, name='projects'),
]
