"""travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from cities.views import pageNotFound
from travel.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('charts/', include(('charts.urls', 'charts'))),
    path('cities/', include(("cities.urls", 'cities'))),
    path('trains/', include(('trains.urls', "trains"))),
    path('routes/', include(('routes.urls', "routes"))),

]

handler404 = pageNotFound

handler500 = 'travel.views.custom_error_view'
handler403 = 'travel.views.custom_permission_denied_view'
handler400 = 'travel.views.custom_bad_request_view'