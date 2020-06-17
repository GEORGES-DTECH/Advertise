from django.shortcuts import render
from django.urls import reverse_lazy


from .models import Blog
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class Bloghomeview(ListView):
    model = Blog
    template_name = 'blog/bloghome.html'
    context_object_name = 'blogs'
    ordering = ['-date_posted']


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blogdetails.html'
    context_object_name = 'blog'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    
    template_name = 'blog/blog_form.html'
    fields = ['title','body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    template_name = 'blog/blog_form.html'
    fields = ['title','body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        else:
            return False


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    context_object_name = 'blog'
    success_url = reverse_lazy('bloghome')

    def test_func(self):
        blog= self.get_object()
        if self.request.user == blog.author:
            return True
        else:
            return False



    