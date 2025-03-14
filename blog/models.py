from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

#class Ticket(models.Model):
 #   ticket_holder = models.ForeignKey(
  #      User,
   #     on_delete=models.CASCADE,
    #    related_name="users_tickets"
    #)
    #date_issued = models.DateTimeField(auto_now_add=True)
    #event = models.ForeignKey(
     #   Event,
      #  on_delete=models.CASCADE,
       # related_name="event_tickets"
    #)

    #def __str__(self):
     #   return f"Ticket for {self.ticket_holder}"

class Comment(models.Model):
    #...
    #challenge = models.SlugField()
    #...
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)