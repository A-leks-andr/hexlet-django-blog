from django.shortcuts import redirect
from django.urls import path, reverse_lazy
from .views import IndexView

app_name = "article"
urlpatterns = [
    path("articles/<str:tags>/<int:article_id>/",
         IndexView.as_view(), name="article"),
    path("", lambda request: redirect(reverse_lazy(
        "article", kwargs={"tags": "python", "article_id": 42})),
        name="home"),
]
