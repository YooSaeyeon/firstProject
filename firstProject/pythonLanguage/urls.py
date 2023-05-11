from django.urls import path
from pythonLanguage import views

urlpatterns = [
    path('', views.pythonLanguage, name='pythonLanguage'),
]