from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from accounts.models import Account
from accounts.thread import SendAccountActivationEmail
import random


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
                user.otp = ''
                user.save()
                print('successfully activate your email.')
                return redirect('accounts:login_view')
        except Exception as e:
            print(e)
        return redirect('accounts:login_view')


class PasswordResetView(TemplateView):
    template_name = "password_reset/password_reset.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        try:
            email = request.POST.get('email')
            user = Account.objects.filter(email=email).first()
            if not user:
                messages.success(request, 'User Not Found.')
                return redirect('accounts:login_view')
            user_obj = Account.objects.get(email=email)
            otp = str(random.randint(100000, 999999))
            user_obj.otp = otp
            user_obj.save()
            title = 'Password reset activation code.'
            SendAccountActivationEmail(user_obj.email, otp, title).start()
            messages.info(request, "Your password reset successful send otp Check your email and submit the otp.")
            return redirect("accounts:password_reset_otp_view")
        except Exception as e:
            print(e)


class EmailPasswordResetVerifyView(TemplateView):
    template_name = 'accounts/check-otp.html'

    def get(self, request):
        return render(request, self.template_name)

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
                print('You both password should be equal.')
                return redirect('accounts:password_reset_confirm_view', otp=otp)
            user.set_password(new_password1)
            user.otp = ''
            user.save()
            print('Successfully your password reset.')
            return redirect('accounts:login_view')
    except Exception as e:
        print(e)
    return render(request, 'password_reset/password_reset_confirm.html')

'''
class PasswordResetConfirmationTemplateView(TemplateView):
    def get(self, request, otp):
        return render(request, 'password_reset/password_reset_confirm.html')

    def post(self, request):
        try:
            new_password1 = request.POST.get('new_password1')
            new_password2 = request.POST.get('new_password2')
            user = Account.objects.get(otp=otp)
            if user:
                if not user.is_active:
                    print('Your Account is not Activate.')
            if new_password1 != new_password2:
                print('You both password should be equal.')
                return redirect('accounts:password_reset_confirm_view', otp=otp)
            user.set_password(new_password1)
            user.otp = ''
            user.save()
            print('Successfully your password reset.')
            return redirect('accounts:login_view')
        except Exception as e:
            print(e)
'''