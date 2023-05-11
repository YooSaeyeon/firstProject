from django.urls import path
from contacted import views

urlpatterns = [
    path('', views.contacted, name='contacted'),
    #path('create/', views.create, name='create'),
]