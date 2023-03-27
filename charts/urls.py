from django.urls import path
from .views import *


urlpatterns = [
    # path('upload/', upload, name='upload'),
    # path('download/', download, name='download'),
    # path('import/', import_data, name='import'),
    path('', chart_test, name='home'),
    path('detail/<str:post_str>/<str:date_str>/', chart_detail, name='charts_detail'),
    path('import_data_to_bd/', import_data_to_bd, name='import_excel'),
    # path('create/', create_chart, name='create'),
    path('add_chart/', add_chart, name='add_chart')
]