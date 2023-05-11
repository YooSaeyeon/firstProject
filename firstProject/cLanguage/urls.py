from django.urls import path
from cLanguage import views

urlpatterns = [
    path('', views.cLanguage, name='cLanguage'),
]