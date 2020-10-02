from . import views
from django.urls import path

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:post_pk>/', views.detail, name='detail'),
    path('<int:post_pk>/delete', views.delete, name='delete'),
    path('<int:post_pk>/update', views.update, name='update'),
]
