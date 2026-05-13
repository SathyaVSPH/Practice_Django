# ~ from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
# ~ def homepage_view(request):
    # ~ posts = Post.objects.all()
    # ~ return render(request, "home.html", {"posts" : posts})
    
class PostList(ListView):
	model = Post
	template_name = "home.html"
