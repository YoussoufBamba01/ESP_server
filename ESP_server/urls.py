
from django.contrib import admin
from django.urls import path
from data_administration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('post/', views.post, name='post'),
    
]
