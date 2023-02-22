from django.urls import path
from .views import *


urlpatterns = [
    path('', CityListView.as_view(), name='home'),
    path('detail/<slug:slug>/', CityDetailView.as_view(), name='detail'),
    path('create/', CityCreateView.as_view(), name='create'),
    path('update/<slug:slug>/', CityUpdateView.as_view(), name='update'),
    path('delete/<slug:slug>/', CityDeleteView.as_view(), name='delete'),
]