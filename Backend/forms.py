from django import forms
from django.contrib.auth import get_user_model

from .models import Machine, Maintenance


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
        self.fields['machine'].label = 'Модель техники'
        self.fields['service_company'].queryset = User.objects.filter(role='SC')
