

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recherche', views.index2, name="recherche"),
    path('get', views.get, name="get"),
    path('about', views.about, name="about"),
    path('index4', views.index4, name="avance"),
    path('advance', views.advanced, name="advance"),


]