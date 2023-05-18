from django.urls import path
from pythonLanguage import views

urlpatterns = [
    path('', views.pythonLanguage, name='pythonLanguage'),
    path('create_p/', views.create_p, name='create_p'),
    path('post_detail_p/<int:id>/', views.post_detail_p, name='post_detail_p'),
    path('update_p/<int:id>/', views.post_update_p, name='post_update_p'),
    path('delete_p/<int:id>/', views.post_delete_p, name='post_delete_p'),
]