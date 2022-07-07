from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms.merchant import CustomerRegisterForm


class MarchentRegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = CustomerRegisterForm 
    success_url = reverse_lazy('accounts:verification_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.is_active = False
        instance.save()
        messages.info(self.request, 'Check Your Email For Account Activation Link.')
        return super(MarchentRegisterView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Customer Register Form'
        return context
