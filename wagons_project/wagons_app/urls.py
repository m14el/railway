from django.urls import path
from .views import WagonListCreateView, WagonDetailView

urlpatterns = [
    path('wagons/', WagonListCreateView.as_view(), name='wagon-list-create'),
    path('wagons/<int:pk>/', WagonDetailView.as_view(), name='wagon-detail'),
]