from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models.branch import Branch
from ..forms.branch import BranchForm


class BranchCreateAndListView(LoginRequiredMixin, ListView):
    model = Branch
    template_name = 'branch/list.html'
    success_url = '/branch/'


class BranchCreateView(LoginRequiredMixin, CreateView):
    model = Branch
    form_class = BranchForm
    template_name = 'common_form/create-and-update.html'
    success_url = '/branch/'

    def get_context_data(self, **kwargs):
        context = super(BranchCreateView, self).get_context_data(**kwargs)
        context["title"] = 'Create a Branch'
        return context


class BranchUpdateView(LoginRequiredMixin, UpdateView):
    model = Branch
    form_class = BranchForm
    template_name = 'common_form/create-and-update.html'
    success_url = '/branch/'

    def get_context_data(self, **kwargs):
        context = super(BranchUpdateView, self).get_context_data(**kwargs)
        context["title"] = 'Update Branch'
        return context


class BranchDeleteView(LoginRequiredMixin, DeleteView):
    model = Branch
    success_url = '/branch/'
    
