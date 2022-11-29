from django.urls import path

from .views import Index, MachineDetail

urlpatterns = [
    path('', Index.as_view()),
    path('machine/<int:pk>/', MachineDetail.as_view(), name='machine_detail'),
]
