from django.urls import path
from . import views

urlpatterns = [
	path("", views.AllPosts.as_view(), name="home"),
]
