from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse_lazy
from .thread import SendAccountActivationEmail
from helpers.utils import SIX_NUMBER
from .forms import CustomerRegisterForm, RiderRegisterForm, ManagerRegisterForm
from .models import Account
from .mixins import ManagerRequiredMixin


class AccountListView(ManagerRequiredMixin, ListView):
    model = Account
    template_name = "accounts/users.html"


class CustomerRegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = CustomerRegisterForm 
    success_url = reverse_lazy('accounts:verification_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.is_active = False
        instance.save()
        messages.info(self.request, 'Check Your Email For Account Activation Link.')
        return super(CustomerRegisterView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Customer Register Form'
        return context

class RiderRegisterView(ManagerRequiredMixin, CreateView):
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

class ManagerRegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = ManagerRegisterForm 
    success_url = reverse_lazy('accounts:verification_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.is_active = False
        instance.save()
        messages.info(self.request, 'Check Your Email For Account Activation Link.')
        return super(ManagerRegisterView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Customer Register Form'
        return context

class EmailVerifyView(TemplateView):
    template_name = 'accounts/check-otp.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        try:
            otp = request.POST.get('otp')
            user = Account.objects.filter(otp__iexact=otp).first()
            if user.is_active:
                print('already activated your email.')
            else:
                user.is_active = True
                user.save()
                print('succesfully activate your email.')
                return redirect('accounts:login_view')
        except Exception as e:
            print('===============================================')
            print(e)
        return redirect('accounts:login_view')

class LoginView(TemplateView):
    template_name = 'accounts/login.html'
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('percels:dashboard_view')
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            phone_number = request.POST.get('phone_number')
            password = request.POST.get('password')
            user = authenticate(request, phone_number=phone_number, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.info(request, "successfylly login.")
                    return redirect('percels:dashboard_view')
                else:
                    messages.info(request, "Please check your mail and verification the link.")
                    return render(request, self.template_name)
            else:
                messages.info(request, "Invalid Login.")
                return render(request, self.template_name)

class LogoutView(TemplateView):
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('accounts:login_view')

class PasswordResetView(TemplateView):
    template_name="password_reset/password_reset.html"
    
    def post(self, request, *args, **kwargs):
        try:
            email = request.POST.get('email')
            user = Account.objects.filter(email=email).first()
            if not user:
                messages.success(request, 'User Not Found.')
                print('erros oooooooooooooooooooooooo')
                return redirect('accounts:login_view')
            user_obj = Account.objects.get(email=email)
            otp = str(SIX_NUMBER)
            user_obj.otp = otp
            user_obj.save()
            SendAccountActivationEmail(user_obj.email, otp).start()
            print('pk ppppppppppppppppppppppppppp')
            messages.info(request,
            "Your password reset sccessfull send otp Cehck your email and submit the otp.")
            return redirect("accounts:password_reset_otp_view")
        except Exception as e:
            print(e)
            print('No Thaking')

class EmailPasswordResetVerifyView(TemplateView):
    template_name = 'accounts/check-otp.html'
    def post(self, request):
        try:
            otp = request.POST.get('otp')
            user = Account.objects.get(otp__iexact=otp)
            if user:
                if not user.is_active:
                    print('Your Account not Activate.')
                else:
                    return redirect('accounts:password_reset_confirm_view', otp=otp)
        except Exception as e:
            print(e)
    
def password_reset_confirmation_view(request, otp):
    try:
        if request.method == 'POST':
            new_password1 = request.POST.get('new_password1')
            new_password2 = request.POST.get('new_password2')
            user = Account.objects.get(otp=otp)
            if user:
                if not user.is_active:
                    print('Your Account is not Activate.')
            if new_password1 != new_password2:
                print('You both password shoud be equal.')
                return redirect('accounts:password_reset_confirm_view', otp=otp)
            user.set_password(new_password1)
            user.save()
            print('Succesfully your password reset.')
            print(f'--------------{otp}------------')
            return redirect('accounts:login_view')
    except Exception as e:
        print(e)
    return render(request, 'password_reset/password_reset_confirm.html')

# class EmailPasswordResetConformView(TemplateView):
#     template_name = 'password_reset/password_reset_confirm.html'
#     def get(self, request, otp):
#         user = Account.objects.get(otp__iexact=otp)
#         return render(request, self.template_name)

#     def post(self, request, *args, **kwargs):
#         try:
#             new_password1 = request.POST.get('new_password1')
#             new_password2 = request.POST.get('new_password2')
#             otp = kwargs.get('otp')
#             user = Account.objects.get(otp=otp)
#             if user:
#                 if not user.is_active:
#                     print('Your Account not Activate.')
#             else:
#                 if new_password1 != new_password2:
#                     print('You both password shoud be equal.')
#                     return redirect('accounts:password_reset_confirm_view', otp=otp)
#                 user.set_password(new_password1)
#                 user.save()
#                 print('Succesfully your password reset.')
#                 print(f'--------------{otp}------------')
#                 return redirect('accounts:login_view')
#         except Exception as e:
#             print(e)


