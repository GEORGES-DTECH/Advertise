from django.shortcuts import render
from django.urls import reverse_lazy


from .models import Biography
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class Photohomeview(ListView):
    model = Biography
    template_name = 'album/albumhome.html'
    context_object_name = 'photos'
    ordering = ['-date_posted']


class PhotoDetailView(DetailView):
    model = Biography
    template_name = 'album/details.html'
    context_object_name = 'photo'


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Biography
    
    template_name = 'album/album_form.html'
    fields = ['family_member_name', 'description', 'location', 'contact',
               'photo']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PhotoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Biography
    template_name = 'album/album_form.html'
    fields =  ['family_member_name', 'description', 'location', 'contact',
               'photo']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        photo = self.get_object()
        if self.request.user == photo.author:
            return True
        else:
            return False


class PhotoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Biography
    template_name = 'album/album_confirm_delete.html'
    context_object_name = 'photo'
    success_url = reverse_lazy('photohome')

    def test_func(self):
        photo= self.get_object()
        if self.request.user == photo.author:
            return True
        else:
            return False



    