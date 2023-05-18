from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('about/', include('about.urls'), name='about'),
    path('contacted/', include('contacted.urls'), name='contacted'),
    path('cLanguage/', include('cLanguage.urls'), name='cLanguage'),
    path('javaLanguage/', include('javaLanguage.urls'), name='javaLanguage'),
    path('pythonLanguage/', include('pythonLanguage.urls'), name='pythonLanguage'),
    path('etcLanguage/', include('etcLanguage.urls'), name='etcLanguage'),
]
