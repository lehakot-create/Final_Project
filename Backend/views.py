from allauth.account.views import LoginView
from django.views.generic import ListView

from .filters import MachineFilter
from .models import Machine


class Index(ListView):
    model = Machine
    template_name = 'first_page.html'
    context_object_name = 'machine'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = MachineFilter(self.request.GET, queryset=self.get_queryset())
        return context


class MyLogin(LoginView):
    template_name = 'account/login.html'
