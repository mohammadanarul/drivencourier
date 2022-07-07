from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms.rider import RiderRegisterForm


class RiderRegisterView(LoginRequiredMixin, CreateView):
    template_name = 'accounts/register.html'
    form_class = RiderRegisterForm 
    success_url = reverse_lazy('accounts:verification_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.is_active = False
        instance.save()
        messages.info(self.request, 'Check Your Email For Account Activation Link.')
        return super(RiderRegisterView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Rider Register Form'
        return context
