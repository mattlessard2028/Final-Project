from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleCreateView,
    HomeView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),            # Homepage, e.g. /
    path("articles/", ArticleListView.as_view(), name="article_list"),  # Articles list
    path("new/", ArticleCreateView.as_view(), name="article_new"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
]

