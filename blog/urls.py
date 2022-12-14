from django.urls import path
from . import views
from .views import PostList, PostDetail, PostLike, UpdatePost, DeletePost, AddPost, AddCategory

"""
Thanks to Code Institutes 'I Think Therefore I Blog'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/Django3blog
"""

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('add_post/new', views.AddPost.as_view(), name='add_post'),
    path('add_category/new', views.AddCategory.as_view(), name='add_category'),
    path('<slug:slug>/edit/', views.UpdatePost.as_view(), name='update_post'),
    path(
        '<slug:slug>/delete/', views.DeletePost.as_view(), name='delete_post'
        ),
]
