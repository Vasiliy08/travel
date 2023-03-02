from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import *
from django.http import HttpResponseNotFound
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView


__all__ = ("CityListView", 'CityDetailView', 'CityCreateView', 'CityUpdateView', 'CityDeleteView')

class CityListView(ListView):
    paginate_by = 8
    model = City
    template_name = 'cities/home.html'
    context_object_name = 'qs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Города'
        return context

class CityDetailView(DetailView):
    model = City
    template_name = 'cities/detail.html'
    context_object_name = 'qs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Город {context.get("object")}'
        return context

class CityCreateView(SuccessMessageMixin, CreateView):
    form_class = CityForm
    model = City
    template_name = 'cities/create.html'
    context_object_name = 'form'
    success_url = reverse_lazy('cities:home')
    success_message = 'Город успешно создан'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Добавить город'
        return context

class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')
    success_message = 'Город успешно отредактирован'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Обновить город {context.get('object')}"
        return context

class CityDeleteView(SuccessMessageMixin, DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')
    success_message = 'Город успешно удалён'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Удалить город {context.get('object')}"
        return context

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')