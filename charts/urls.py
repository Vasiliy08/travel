from django.urls import path
from .views import *


urlpatterns = [
    path('upload/', upload, name='upload'),
    path('download/', download, name='download'),
    path('import/', import_data, name='import'),
    path('', chart_test, name='home')
]