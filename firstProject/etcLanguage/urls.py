from django.urls import path
from etcLanguage import views

urlpatterns = [
    path('', views.etcLanguage, name='etcLanguage'),
]