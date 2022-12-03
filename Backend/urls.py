from django.urls import path, include
from rest_framework import routers

from .views import Index, MachineDetail, CreateMachineView, CreateMaintenanceView, CreateClaimView, MachineApiView, \
    MaintenanceApiView, ClaimsApiView, directory, ModelsMachineListView, ModelsEngineListView, \
    ModelsTransmissionListView, ModelsDriveAxleListView, ModelsSteeringBridgeListView, TypeMaintenanceListView, \
    RecoveryMethodListView, FailureNodeListView

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

    path('models_machine/', ModelsMachineListView.as_view(), name='models_machine'),
    path('models_engine/', ModelsEngineListView.as_view(), name='models_engine'),
    path('models_transmission/', ModelsTransmissionListView.as_view(), name='models_transmission'),
    path('models_driveaxle/', ModelsDriveAxleListView.as_view(), name='models_driveaxle'),
    path('models_steeringbridge/', ModelsSteeringBridgeListView.as_view(), name='models_steeringbridge'),
    path('models_typemaintenance/', TypeMaintenanceListView.as_view(), name='models_typemaintenance'),
    path('models_recoverymethod/', RecoveryMethodListView.as_view(), name='models_recoverymethod'),
    path('models_failurenode/', FailureNodeListView.as_view(), name='models_failurenode'),

    path('api/v1/', include(router.urls)),
]
