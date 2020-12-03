from django.shortcuts import render
from .models import Post
from django.urls import reverse
from django.views.generic import (ListView,
                                  DetailView
)


class PostListView(ListView):
        model = Post
        template_name = 'blog/blog.html'
        context_object_name ='posts'
        ordering =['-date']
        paginate_by = 5



class PostDetailView(DetailView):
    model = Post
  