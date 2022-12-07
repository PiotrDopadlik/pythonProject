from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('another/', views.url, name = 'anotherurl'),
    path('linkfile/', views.fromFileHTML, name='fromFileHTML')
]