
from django.urls import path
from . import views


urlpatterns = [
        path('', views.all_blog, name='all_blogs'),
    
]