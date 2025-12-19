from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"

# Article views
class ArticleListView(ListView):
    model = Article
    template_name = "articles/article_list.html"  # include "articles/" if inside that folder


class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/article_detail.html"


class ArticleCreateView(CreateView):
    model = Article
    template_name = "articles/article_new.html"
    fields = ("title", "body", "author")


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "articles/article_edit.html"
    fields = ("title", "body")


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "articles/article_delete.html"
    success_url = reverse_lazy("article_list")




# Create your views here.
