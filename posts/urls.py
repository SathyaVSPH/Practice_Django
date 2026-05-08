from django.urls import path
from . import views

urlpatterns = [
    # ~ path("", views.homepage_view, name="home"),
    path("", views.PostList.as_view(), name="posts_list"),
]
