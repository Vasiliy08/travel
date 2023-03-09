from django.urls import path
from .views import *


urlpatterns = [
    path('', RouteListView.as_view(), name='home'),
    path('detail/<slug:slug>/', RouteDetailView.as_view(), name='detail'),
    path('create/', RouteCreateView.as_view(), name='create'),
    path('update/<slug:slug>/', RouteUpdateView.as_view(), name='update'),
    path('delete/<slug:slug>/', RouteDeleteView.as_view(), name='delete'),
    path('search_routes/', search_routes, name='search_routes'),
]