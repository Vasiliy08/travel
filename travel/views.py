from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render


@login_required
def home(request):
    return render(request, 'base.html')

def custom_error_view(request, exception=None):

    return HttpResponseNotFound('Страница не найдена')

def custom_permission_denied_view(request, exception=None):
    return render(request, "errors/403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "errors/400.html", {})