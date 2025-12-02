from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from hexlet_django_blog.article.models import Article


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, "articles/index.html", context={"articles": articles})


class ArticleTagsId(View):
    def get(self, request, *args, **kwargs):
        tags = self.kwargs["tags"]
        article_id = self.kwargs["article_id"]
        return HttpResponse(f"Статья номер {article_id}. Тег {tags}")


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        return render(
            request,
            "articles/show.html",
            context={
                "article": article,
            },
        )
