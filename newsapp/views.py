from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime, date

def home(request):
    return render(request, 'home.html',{})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 6
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'