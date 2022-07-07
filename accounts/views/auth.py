from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'accounts/login.html'
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard_view')
        return render(request, self.template_name)
    
    def post(self, request):
        if request.method == 'POST':
            phone_number = request.POST.get('phone_number')
            password = request.POST.get('password')
            user = authenticate(request, phone_number=phone_number, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.info(request, "successfully login.")
                    return redirect('dashboard_view')
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
