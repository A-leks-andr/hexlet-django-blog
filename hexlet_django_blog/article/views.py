from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from hexlet_django_blog.article.models import Article
from hexlet_django_blog.article.forms import CreateArticle, ArticleForm
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
    template_name = "articles/create.html"

    def get(self, request, *args, **kwargs):
        form = CreateArticle()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = CreateArticle(request.POST)
        if form.is_valid():
            form.save()
            article_name = form.cleaned_data["name"]
            messages.success(request, f'Статья "{article_name}" сохранена')
            return redirect(reverse("article"))
        else:
            return render(request, self.template_name, {"form": form})


class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(
            request, "articles/update.html", {"form": form, "article_id": article_id}
        )

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            article_name = form.cleaned_data["name"]
            messages.success(request, f'Статья "{article_name}" изменена')
            return redirect("article")

        return render(
            request, "articles/update.html", {"form": form, "article_id": article_id}
        )


class ArticleFormDeleteView(View):
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        if article:
            article_name = article.name
            article.delete()
            messages.success(request, f'Статья "{article_name}" удалена')
        return redirect("article")
