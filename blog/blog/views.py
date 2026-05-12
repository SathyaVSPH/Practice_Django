from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from . import models

# Create your views here.
# ~ def all_posts(request):
	# ~ posts = models.Post.objects.all()
	# ~ return render(request, "all_posts.html", {"post_list":posts})

class AllPosts(ListView):
	model = models.Post
	template_name = "all_posts.html"	 


def post_details(request, pk):
	post = get_object_or_404(models.Post, pk=pk)
	return render(request, "post_page.html", {"post":post})
