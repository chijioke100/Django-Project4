from django.shortcuts import render
from django.views import generic
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
#from .models import Event
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


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    comment_form = CommentForm()


    return render(
        request,
        "blog/post_detail.html",
        {"post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        
        },
    )


    


     


   
