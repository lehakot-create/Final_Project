from allauth.account.views import LoginView
from django.views.generic import ListView

from .filters import MachineFilter, AuthMachineFilter
from .models import Machine


class Index(ListView):
    model = Machine
    template_name = 'first_page.html'
    context_object_name = 'machine'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            params = self.request.GET
            if any([params.get('models_machine'), params.get('models_engine'), params.get('model_transmission'),
                   params.get('models_drive_axle'), params.get('models_steering_bridge')]):
                return Machine.objects.all()
        else:
            if self.request.GET.get('factory_number_machine'):
                return self.queryset
        return Machine.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['filter_auth_machine'] = AuthMachineFilter(self.request.GET, queryset=self.get_queryset())
            return context
        context['filter'] = MachineFilter(self.request.GET, queryset=self.get_queryset())
        return context


class MyLogin(LoginView):
    template_name = 'account/login.html'
