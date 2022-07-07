import threading
from django.conf import settings
from django.core.mail import send_mail


class SendAccountActivationEmail(threading.Thread):
    
    def __init__(self, email, otp, title):
        self.email = email
        self.otp = otp
        self.title = title
        threading.Thread.__init__(self)
    
    def run(self):
        try:
            subject = f'{self.title}'
            message = f'Hi , click on the link to activate your password OTP: {self.otp}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [self.email]
            send_mail(subject, message, email_from, recipient_list)
        except Exception as e:
            print(e)
