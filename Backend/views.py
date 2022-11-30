from allauth.account.views import LoginView
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .filters import MachineFilter, AuthMachineFilter, AuthMaintenanceFilter, AuthClaimFilter
from .forms import MachineForm, MaintenanceForm
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
            if self.request.user.role == 'MN':
                context['filter_auth_machine'] = AuthMachineFilter(self.request.GET,
                                                                   queryset=Machine.objects.all())
                context['filter_auth_maintenance'] = AuthMaintenanceFilter(self.request.GET,
                                                                           queryset=Maintenance.objects.all())
                context['filter_auth_claim'] = AuthClaimFilter(self.request.GET,
                                                               queryset=Claims.objects.all())
                return context
            elif self.request.user.role == 'CL':
                context['filter_auth_machine'] = AuthMachineFilter(self.request.GET,
                                                                   queryset=Machine.objects.filter(
                                                                       client=self.request.user
                                                                   ))
                context['filter_auth_maintenance'] = AuthMaintenanceFilter(self.request.GET,
                                                                           queryset=Maintenance.objects.filter(
                                                                               machine__client=self.request.user
                                                                           ))
                context['filter_auth_claim'] = AuthClaimFilter(self.request.GET,
                                                               queryset=Claims.objects.filter(
                                                                   machine__client=self.request.user
                                                               ))
                return context
            elif self.request.user.role == 'SC':
                context['filter_auth_machine'] = AuthMachineFilter(self.request.GET,
                                                                   queryset=Machine.objects.filter(
                                                                       service_company=self.request.user
                                                                   ))
                context['filter_auth_maintenance'] = AuthMaintenanceFilter(self.request.GET,
                                                                           queryset=Maintenance.objects.filter(
                                                                               service_company=self.request.user
                                                                           ))
                context['filter_auth_claim'] = AuthClaimFilter(self.request.GET,
                                                               queryset=Claims.objects.filter(
                                                                   machine__service_company=self.request.user
                                                               ))
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


class CreateMachineView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('Backend.add_machine',)
    template_name = 'create.html'
    form_class = MachineForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        User = get_user_model()
        form.instance.client = User.objects.get(id=self.request.user.id)
        return super(CreateMachineView, self).form_valid(form)


class CreateMaintenanceView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('Backend.add_maintenance',)
    template_name = 'create.html'
    form_class = MaintenanceForm
    success_url = reverse_lazy('index')
