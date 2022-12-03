from django import forms
from django.contrib.auth import get_user_model

from .models import Machine, Maintenance, Claims, ModelsMachine, ModelsEngine, ModelsTransmission, ModelsDriveAxle, \
    ModelsSteeringBridge, TypeMaintenance, RecoveryMethod, FailureNode


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = '__all__'
        exclude = ('client',)
        widgets = {
            'date_of_shipment': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'})
        }

    def __init__(self, *args, **kwargs):
        User = get_user_model()
        super(MachineForm, self).__init__(*args, **kwargs)
        self.fields['service_company'].queryset = User.objects.filter(role='SC')


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = '__all__'

        widgets = {
            'date_maintenance': forms.DateInput(format=('%d/%m/%Y'),
                                                attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                       'type': 'date'}),
            'date_work_order': forms.DateInput(format=('%d/%m/%Y'),
                                               attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                      'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        User = get_user_model()
        super(MaintenanceForm, self).__init__(*args, **kwargs)
        self.fields['service_company'].queryset = User.objects.filter(role='SC')


class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claims
        fields = '__all__'
        widgets = {
            'date_of_rejection': forms.DateInput(format=('%d/%m/%Y'),
                                                attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                       'type': 'date'}),
            'date_recovery': forms.DateInput(format=('%d/%m/%Y'),
                                               attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                      'type': 'date'})
        }


class ModelsMachineForm(forms.ModelForm):
    class Meta:
        model = ModelsMachine
        fields = '__all__'


class ModelsEngineForm(forms.ModelForm):
    class Meta:
        model = ModelsEngine
        fields = '__all__'


class ModelsTransmissionForm(forms.ModelForm):
    class Meta:
        model = ModelsTransmission
        fields = '__all__'


class ModelsDriveAxleForm(forms.ModelForm):
    class Meta:
        model = ModelsDriveAxle
        fields = '__all__'


class ModelsSteeringBridgeForm(forms.ModelForm):
    class Meta:
        model = ModelsSteeringBridge
        fields = '__all__'


class TypeMaintenanceForm(forms.ModelForm):
    class Meta:
        model = TypeMaintenance
        fields = '__all__'


class RecoveryMethodForm(forms.ModelForm):
    class Meta:
        model = RecoveryMethod
        fields = '__all__'


class FailureNodeForm(forms.ModelForm):
    class Meta:
        model = FailureNode
        fields = '__all__'
