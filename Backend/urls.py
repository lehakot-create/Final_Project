from django.urls import path

from .views import Index, MachineDetail, CreateMachineView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('machine/<int:pk>/', MachineDetail.as_view(), name='machine_detail'),
    path('machine_create/', CreateMachineView.as_view(), name='machine_create'),
]
