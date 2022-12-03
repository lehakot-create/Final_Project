from allauth.account.views import LoginView
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from rest_framework import viewsets

from .filters import MachineFilter, AuthMachineFilter, AuthMaintenanceFilter, AuthClaimFilter
from .forms import MachineForm, MaintenanceForm, ClaimForm
from .models import Machine, Maintenance, Claims, ModelsMachine, ModelsEngine, ModelsTransmission, ModelsDriveAxle, \
    ModelsSteeringBridge, TypeMaintenance, RecoveryMethod, FailureNode
from .serializers import MachineSerializer, MaintenanceSerializer, ClaimsSerializer


def directory(request):
    return render(request, 'directory.html')


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


class ModelsMachineListView(ListView):
    model = ModelsMachine
    template_name = 'directory.html'
    context_object_name = 'models'


class ModelsEngineListView(ListView):
    model = ModelsEngine
    template_name = 'directory.html'
    context_object_name = 'models'


class ModelsTransmissionListView(ListView):
    model = ModelsTransmission
    template_name = 'directory.html'
    context_object_name = 'models'


class ModelsDriveAxleListView(ListView):
    model = ModelsDriveAxle
    template_name = 'directory.html'
    context_object_name = 'models'


class ModelsSteeringBridgeListView(ListView):
    model = ModelsSteeringBridge
    template_name = 'directory.html'
    context_object_name = 'models'


class TypeMaintenanceListView(ListView):
    model = TypeMaintenance
    template_name = 'directory.html'
    context_object_name = 'models'


class RecoveryMethodListView(ListView):
    model = RecoveryMethod
    template_name = 'directory.html'
    context_object_name = 'models'


class FailureNodeListView(ListView):
    model = FailureNode
    template_name = 'directory.html'
    context_object_name = 'models'


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


class CreateClaimView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('Backend.add_claims',)
    template_name = 'create.html'
    form_class = ClaimForm
    success_url = reverse_lazy('index')


class MachineApiView(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer


class MaintenanceApiView(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer


class ClaimsApiView(viewsets.ModelViewSet):
    queryset = Claims.objects.all()
    serializer_class = ClaimsSerializer
