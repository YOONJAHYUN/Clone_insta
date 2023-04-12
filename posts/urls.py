from . import views
from django.urls import path


app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('post/', views.detail, name='post'),
    path('<int:post_pk>/delete/', views.delete, name='delete'),
    
    ]
