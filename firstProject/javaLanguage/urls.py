from django.urls import path
from javaLanguage import views

urlpatterns = [
    path('', views.javaLanguage, name='javaLanguage'),
]