from django.urls import path
from cLanguage import views

urlpatterns = [
    path('', views.cLanguage, name='cLanguage'),
    path('create_c/', views.create_c, name='create_c'),
    path('post_detail_c/<int:id>/', views.post_detail_c, name='post_detail_c'),
    path('update_c/<int:id>/', views.post_update_c, name='post_update_c'),
    path('delete_c/<int:id>/', views.post_delete_c, name='post_delete_c'),
]