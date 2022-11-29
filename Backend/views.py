from allauth.account.views import LoginView
from django.views.generic import ListView, DetailView

from .filters import MachineFilter, AuthMachineFilter, AuthMaintenanceFilter, AuthClaimFilter
from .models import Machine, Maintenance, Claims


class Index(ListView):
    model = Machine
    template_name = 'first_page.html'
    context_object_name = 'machine'

    def get_queryset(self):
        if self.request.GET.get('factory_number_machine'):
            return self.queryset
        return Machine.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['filter_auth_machine'] = AuthMachineFilter(self.request.GET,
                                                               queryset=Machine.objects.all())
            context['filter_auth_maintenance'] = AuthMaintenanceFilter(self.request.GET,
                                                                       queryset=Maintenance.objects.all())
            context['filter_auth_claim'] = AuthClaimFilter(self.request.GET,
                                                           queryset=Claims.objects.all())
            return context
        context['filter'] = MachineFilter(self.request.GET, queryset=self.get_queryset())
        return context


class MyLogin(LoginView):
    template_name = 'account/login.html'


class MachineDetail(DetailView):
    model = Machine
    template_name = 'machine_detail.html'
    context_object_name = 'machine'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['machine_maintenance'] = Maintenance.objects.filter(machine=self.kwargs.get('pk'))
        context['machine_claim'] = Claims.objects.filter(machine=self.kwargs.get('pk'))
        return context
