from django.urls import path, include
from rest_framework import routers

from .views import Index, MachineDetail, CreateMachineView, CreateMaintenanceView, CreateClaimView, MachineApiView, \
    MaintenanceApiView, ClaimsApiView, directory

router = routers.DefaultRouter()
router.register('machine', MachineApiView)
router.register('maintenance', MaintenanceApiView)
router.register('claims', ClaimsApiView)

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('machine/<int:pk>/', MachineDetail.as_view(), name='machine_detail'),
    path('machine_create/', CreateMachineView.as_view(), name='machine_create'),
    path('maintenance_create/', CreateMaintenanceView.as_view(), name='maintenance_create'),
    path('claim_create/', CreateClaimView.as_view(), name='claim_create'),

    path('directory/', directory, name='directory'),

    path('api/v1/', include(router.urls)),
]
