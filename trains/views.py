from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import *
from django.http import HttpResponseNotFound
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView


__all__ = ("TrainListView", 'TrainDetailView', 'TrainCreateView', 'TrainUpdateView', 'TrainDeleteView')

class TrainListView(ListView):
    paginate_by = 8
    model = Train
    template_name = 'trains/home.html'
    context_object_name = 'qs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Поезда'
        return context

class TrainDetailView(DetailView):
    model = Train
    template_name = 'trains/detail.html'
    context_object_name = 'qs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Поезд {context.get("object")}'
        return context

class TrainCreateView(SuccessMessageMixin, CreateView):
    form_class = TrainForm
    model = Train
    template_name = 'trains/create.html'
    context_object_name = 'form'
    success_url = reverse_lazy('trains:home')
    success_message = 'Поезд успешно создан'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = f'Добавить поезд'
        return context

class TrainUpdateView(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:home')
    success_message = 'Поезд успешно отредактирован'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Обновить поезд {context.get('object')}"
        return context

class TrainDeleteView(SuccessMessageMixin, DeleteView):
    model = Train
    template_name = 'trains/delete.html'
    success_url = reverse_lazy('trains:home')
    success_message = 'Поезд успешно удалён'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Удалить поезд {context.get('object')}"
        return context

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')
