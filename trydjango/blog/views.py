from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

from .models import Article
from .forms import ArticleModelForm

# class based views
# Create your views here.

class ArticleCreateView(CreateView):
    # <blog>/<modelname>_list.html this one is generic one. system looks for this
    template_name = 'articles/article_create.html' # a way to overwrite generic one
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    # success_url = '/' # a way to overwrite success url

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # default method works really wel for us. just define get_absolute_url method in models
    # a way to overwrite redirect
    # def success_url(self):
    #     return '/'

class ArticleListView(ListView):
    # <blog>/<modelname>_list.html this one is generic one. system looks for this
    template_name = 'articles/article_list.html' # a way to overwrite generic one
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    # <blog>/<modelname>_list.html this one is generic one. system looks for this
    template_name = 'articles/article_detail.html' # a way to overwrite generic one
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    # success_url = '/blog/' # one way to set success url or you can use reverse method 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:article-list')