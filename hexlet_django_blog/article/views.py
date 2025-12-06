from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from hexlet_django_blog.article.models import Article
from hexlet_django_blog.article.forms import CreateArticle
from django.urls import reverse


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


class CreateArticleView(View):
    template_name = 'articles/create.html'

    def get(self, request, *args, **kwargs):
        form = CreateArticle()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CreateArticle(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('article'))
        else:
            return render(request, self.template_name, {'form': form})