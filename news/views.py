from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from news.models import News
from news.forms import NewsForm


class NewsListView(LoginRequiredMixin, ListView):
    model = News
    context_object_name = "news_list"
    extra_context = {"title": "News"}


class NewsCreateView(LoginRequiredMixin, CreateView):
    template_name = "news/news_form.html"
    form_class = NewsForm
    success_url = reverse_lazy("dashboard:news:news-list")
    extra_context = {"title": "Add News"}


class NewsUpdateView(LoginRequiredMixin, UpdateView):
    model = News
    template_name = "news/news_form.html"
    form_class = NewsForm
    success_url = reverse_lazy("dashboard:news:news-list")
    extra_context = {"title": "Update News"}


class NewsDeleteView(LoginRequiredMixin, DeleteView):
    model = News
    success_url = reverse_lazy("dashboard:news:news-list")
