from django.urls import path, include
from rest_framework import routers

from .views import Index, MachineDetail, CreateMachineView, CreateMaintenanceView, CreateClaimView, MachineApiView, \
    MaintenanceApiView, ClaimsApiView, ModelsMachineListView, ModelsEngineListView, \
    ModelsTransmissionListView, ModelsDriveAxleListView, ModelsSteeringBridgeListView, TypeMaintenanceListView, \
    RecoveryMethodListView, FailureNodeListView, ModelsMachineUpdateView, ModelsEngineUpdateView, \
    ModelsTransmissionUpdateView, ModelsDriveAxleUpdateView, ModelsSteeringBridgeUpdateView, TypeMaintenanceUpdateView, \
    RecoveryMethodUpdateView, FailureNodeUpdateView, ModelsMachineCreateView, ModelsEngineCreateView, \
    ModelsTransmissionCreateView, ModelsDriveAxleCreateView, ModelsSteeringBridgeCreateView, TypeMaintenanceCreateView, \
    RecoveryMethodCreateView, FailureNodeCreateView

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

    path('models_machine/<int:pk>/', ModelsMachineUpdateView.as_view(), name='models_machine_update'),
    path('models_engine/<int:pk>/', ModelsEngineUpdateView.as_view(), name='models_engine_update'),
    path('models_transmission_update/<int:pk>/', ModelsTransmissionUpdateView.as_view(), name='models_transmission_update'),
    path('models_driveaxle_update/<int:pk>/', ModelsDriveAxleUpdateView.as_view(), name='models_driveaxle_update'),
    path('models_steeringbridge_update/<int:pk>/', ModelsSteeringBridgeUpdateView.as_view(), name='models_steeringbridge_update'),
    path('models_typemaintenance_update/<int:pk>/', TypeMaintenanceUpdateView.as_view(), name='models_typemaintenance_update'),
    path('models_recoverymethod_update/<int:pk>/', RecoveryMethodUpdateView.as_view(), name='models_recoverymethod_update'),
    path('models_failurenode_update/<int:pk>/', FailureNodeUpdateView.as_view(), name='models_failurenode_update'),

    path('models_machine_create/', ModelsMachineCreateView.as_view(), name='models_machine_create'),
    path('models_engine_create/', ModelsEngineCreateView.as_view(), name='models_engine_create'),
    path('models_transmission_create/', ModelsTransmissionCreateView.as_view(), name='models_transmission_create'),
    path('models_driveaxle_create/', ModelsDriveAxleCreateView.as_view(), name='models_driveaxle_create'),
    path('models_steeringbridge_create/', ModelsSteeringBridgeCreateView.as_view(), name='models_steeringbridge_create'),
    path('models_typemaintenance_create/', TypeMaintenanceCreateView.as_view(), name='models_typemaintenance_create'),
    path('models_recoverymethod_create/', RecoveryMethodCreateView.as_view(), name='models_recoverymethod_create'),
    path('models_failurenode_create/', FailureNodeCreateView.as_view(), name='models_failurenode_create'),

    path('api/v1/', include(router.urls)),
]
