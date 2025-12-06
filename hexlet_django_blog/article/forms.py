from django import forms
from .models import Article


class CreateArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["name", "body"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-input"}),
            "body": forms.Textarea(attrs={"cols": 40, "rows": 10}),
        }

    def clean_name(self):
        name = self.cleaned_data["name"]
        # Проверяем, существует ли статья с таким именем
        if Article.objects.filter(name=name).exists():
            raise forms.ValidationError("Статья с таким заголовком уже существует.")
        return name


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["name", "body"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-input"}),
            "body": forms.Textarea(attrs={"cols": 40, "rows": 10}),
        }
