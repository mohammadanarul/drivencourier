from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Account
from ..forms.auth import AccountForm, AccountUpdateForm


class AccountListView(LoginRequiredMixin, ListView):
    model = Account
    template_name = "accounts/list.html"


class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    form_class = AccountForm
    template_name = 'common_form/create-and-update.html'
    success_url = reverse_lazy('accounts:user_list_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.is_active = False
        instance.save()
        return super(AccountCreateView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(AccountCreateView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(AccountCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Add a User'
        return context


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = Account
    form_class = AccountUpdateForm
    template_name = 'common_form/create-and-update.html'
    success_url = reverse_lazy('accounts:user_list_view')

    def get_context_data(self, **kwargs):
        context = super(AccountUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'User update'
        return context


class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = Account
    success_url = reverse_lazy('accounts:user_list_view')




