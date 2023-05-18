from django.urls import path
from javaLanguage import views

urlpatterns = [
    path('', views.javaLanguage, name='javaLanguage'),
    path('create_j/', views.create_j, name='create_j'),
    path('post_detail_j/<int:id>/', views.post_detail_j, name='post_detail_j'),
    path('update_j/<int:id>/', views.post_update_j, name='post_update_j'),
    path('delete_j/<int:id>/', views.post_delete_j, name='post_delete_j'),
]