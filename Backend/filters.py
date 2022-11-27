from django_filters import FilterSet

from .models import Machine


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
                  'models_drive_axle',
                  'models_steering_bridge',)
