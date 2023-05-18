from django.urls import path
from etcLanguage import views

urlpatterns = [
    path('', views.etcLanguage, name='etcLanguage'),
    path('create_e/', views.create_e, name='create_e'),
    path('post_detail_e/<int:id>/', views.post_detail_e, name='post_detail_e'),
    path('update_e/<int:id>/', views.post_update_e, name='post_update_e'),
    path('delete_e/<int:id>/', views.post_delete_e, name='post_delete_e'),
]