from django.urls import path
from . import views

urlpatterns = [
	path("", views.AllPosts.as_view(), name="home"),
	# path("post/<int:pk>/", views.post_details, name="post"),
    path("post/<int:pk>/", views.PostPage.as_view(), name="post"),
]
