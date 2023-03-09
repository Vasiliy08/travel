from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from routes.models import Route
from routes.utils import get_routes
from .forms import *
from django.http import HttpResponseNotFound
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView


__all__ = ("RouteListView", 'RouteDetailView', 'RouteCreateView', 'RouteUpdateView', 'RouteDeleteView', 'search_routes')


class RouteListView(ListView):
    paginate_by = 8
    model = Route
    template_name = 'routes/home.html'
    context_object_name = 'qs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Маршруты'
        return context


class RouteDetailView(DetailView):
    model = Route
    template_name = 'routes/detail.html'
    context_object_name = 'qs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Маршрут {context.get("object")}'
        return context


class RouteCreateView(SuccessMessageMixin, CreateView):
    form_class = RouteForm
    model = Route
    template_name = 'routes/create.html'
    context_object_name = 'form'
    success_url = reverse_lazy('routes:home')
    success_message = 'Маршрут успешно создан'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = f'Добавить маршрут'
        return context


class RouteUpdateView(SuccessMessageMixin, UpdateView):
    model = Route
    form_class = RouteForm
    template_name = 'routes/update.html'
    success_url = reverse_lazy('routes:home')
    success_message = 'Маршрут успешно отредактирован'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Обновить маршрут {context.get('object')}"
        return context


class RouteDeleteView(SuccessMessageMixin, DeleteView):
    model = Route
    template_name = 'routes/delete.html'
    success_url = reverse_lazy('routes:home')
    success_message = 'Маршрут успешно удалён'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Удалить маршрут {context.get('object')}"
        return context


def search_routes(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as e:
                messages.error(request, e)
                return render(request, 'routes/home.html', {'form': form})
            return render(request, 'routes/home.html', context)
        else:
            messages.error(request, 'Некорректная форма')
            return render(request, 'routes/search_routes.html', {'form': form})
    else:
        form = RouteForm()
        messages.error(request, 'Нет данных для поиска')
        return render(request, 'routes/search_routes.html', {'form': form})


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')
