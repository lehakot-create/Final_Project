from django_filters import FilterSet

from .models import Machine, Maintenance, Claims


class MachineFilter(FilterSet):
    class Meta:
        model = Machine
        fields = ('factory_number_machine',)


class AuthMachineFilter(FilterSet):
    class Meta:
        model = Machine
        fields = ('models_machine',
                  'models_engine',
                  'model_transmission',
                  'models_steering_bridge',
                  'models_drive_axle',)


class AuthMaintenanceFilter(FilterSet):
    class Meta:
        model = Maintenance
        fields = ('type_maintenance',
                  'machine__factory_number_machine',
                  'service_company',)


class AuthClaimFilter(FilterSet):
    class Meta:
        model = Claims
        fields = ('failure_node',
                  'recovery_method',
                  'service_company',)
