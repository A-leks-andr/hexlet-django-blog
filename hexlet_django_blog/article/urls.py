from django.urls import path
from hexlet_django_blog.article import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="article"),
    path(
        "<str:tags>/<int:article_id>/",
        views.ArticleTagsId.as_view(),
        name="article_tags",
    ),
    path("<int:id>", views.ArticleView.as_view(), name="article_id"),
]
