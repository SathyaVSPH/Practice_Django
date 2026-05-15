# from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models

# Create your views here.
# ~ def all_posts(request):
	# ~ posts = models.Post.objects.all()
	# ~ return render(request, "all_posts.html", {"post_list":posts})

class AllPosts(ListView):
	model = models.Post
	template_name = "all_posts.html"	 


""" def post_details(request, pk):
	post = get_object_or_404(models.Post, pk=pk)
	return render(request, "post_page.html", {"post":post}) """
class PostPage(DetailView):
	model = models.Post
	template_name = "post_page.html"


class CreatePost(CreateView):
	model = models.Post
	template_name = "new_post.html"
	fields = ["title", "author", "body"]


class UpdatePost(UpdateView):
	model = models.Post
	template_name = "update_post.html"
	fields = ["title", "body"]


class DeletePost(DeleteView):
	model = models.Post
	template_name = "delete_post.html"
	success_url = reverse_lazy("home")