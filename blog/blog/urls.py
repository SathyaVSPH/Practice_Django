from django.urls import path
from . import views

urlpatterns = [
	path("", views.AllPosts.as_view(), name="home"),
	# path("post/<int:pk>/", views.post_details, name="post"),
    path("post/<int:pk>/", views.PostPage.as_view(), name="post"),
    path("post/new/", views.CreatePost.as_view(), name="create_post"),
    path("post/<int:pk>/edit/", views.UpdatePost.as_view(), name="update_post"),
    path("post/<int:pk>/delete/", views.DeletePost.as_view(), name="delete_post"),
]
