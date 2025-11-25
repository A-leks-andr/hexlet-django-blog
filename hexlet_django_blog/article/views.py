from django.shortcuts import render
from django.views import View


# Create your views here.
class IndexView(View):
    def get(self, request, tags, article_id):
        content = f"Статья номер {article_id}. Тег {tags}"
        return render(request, "articles/index.html", context={"content": content})
