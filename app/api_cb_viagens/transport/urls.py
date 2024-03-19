from django.urls import path
from .views import TransportListView, TransportFilterListView

urlpatterns = [

    path('', TransportListView.as_view(), name='list-trips'),
    path('city/<str:city>/', TransportFilterListView.as_view(), name='list-filter-trips'),

]