from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
class IndexView(View):
    def get(self, request):
        content = "Информация"
        return render(
            request, "articles/index.html",
            context={'content': content}
            )

class ArticleTagsId(View):
    def get(self, request, *args, **kwargs):
        tags = self.kwargs['tags']
        article_id = self.kwargs['article_id']
        return HttpResponse(f'Статья номер {article_id}. Тег {tags}')