from django.shortcuts import render
from django.views import generic
from .models import Post
#from django.http import HttpResponse

# Create your views here.
#def my_blog(request):
 #  return HttpResponse("Hello, blog!")

# Create your views here.
class PostList(generic.ListView):
    #model = Post
    queryset = Post.objects.filter(status=1)
    #template_name = "post_list.html"
    template_name = "blog/index.html"
    paginate_by = 6
    


     


   
