from django.urls import path
from hexlet_django_blog.article.views import (
    IndexView,
    ArticleTagsId,
    ArticleView,
    CreateArticleView,
    ArticleFormEditView,
    ArticleFormDeleteView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="article"),
    path(
        "<str:tags>/<int:article_id>/",
        ArticleTagsId.as_view(),
        name="article_tags",
    ),
    path("<int:id>/delete/", ArticleFormDeleteView.as_view(), name="article_delete"),
    path("<int:id>/edit/", ArticleFormEditView.as_view(), name="article_update"),
    path("<int:id>/", ArticleView.as_view(), name="article_id"),
    path("create/", CreateArticleView.as_view(), name="create_article"),
]
