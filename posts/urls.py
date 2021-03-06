from . import views
from django.urls import path

app_name = 'posts'
urlpatterns = [
    # posts
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:post_pk>/', views.detail, name='detail'),
    path('<int:post_pk>/delete', views.delete, name='delete'),
    path('<int:post_pk>/update', views.update, name='update'),
    # comments
    path('<int:post_pk>/create_comment/', views.create_comment, name='create_comment'),
    path('<int:post_pk>/delete/<int:comment_pk>', views.delete_comment, name='delete_comment'),
    # like
    path('<int:post_pk>/like/<str:before>/', views.like, name='like'),
    # Search
    path('search/', views.search, name='search'),
    path('click_tag/<str:hashtag>', views.click_tag, name='click_tag'),
    # Close
    # path('<int:post_pk>/close/<str:next>/', views.close, name='close'),
]
