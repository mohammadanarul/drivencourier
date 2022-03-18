from django.db.models.signals import post_save
from django.dispatch import receiver
from helpers.utils import SIX_NUMBER
from .thread import SendAccountActivationEmail
from .models import Account, Customer, Rider, Manager


@receiver(post_save, sender=Account)
def send_email_token(sender, instance, created, **kwargs):
    try:
        if not instance.otp:
            otp = str(SIX_NUMBER)
            instance.otp = otp
            ''' EXCEUTING THREAD TO SEND EMAIL '''
            SendAccountActivationEmail(instance.email , otp).start()

    except Exception as e:
        print(e)

@receiver(post_save, sender=Manager)
def send_email_token(sender, instance, created, **kwargs):
    try:
        if not instance.otp:
            otp = str(SIX_NUMBER)
            instance.otp = otp
            instance.save()
            ''' EXCEUTING THREAD TO SEND EMAIL '''
            SendAccountActivationEmail(instance.email , otp).start()

    except Exception as e:
        print(e)

@receiver(post_save, sender=Rider)
def send_email_token(sender, instance, created, **kwargs):
    try:
        if not instance.otp:
            otp = str(SIX_NUMBER)
            instance.otp = otp
            instance.save()
            ''' EXCEUTING THREAD TO SEND EMAIL '''
            SendAccountActivationEmail(instance.email , otp).start()

    except Exception as e:
        print(e)

@receiver(post_save, sender=Customer)
def send_email_token(sender, instance, created, **kwargs):
    try:
        if not instance.otp:
            otp = str(SIX_NUMBER)
            instance.otp = otp
            instance.save()
            ''' EXCEUTING THREAD TO SEND EMAIL '''
            SendAccountActivationEmail(instance.email , otp).start()

    except Exception as e:
        print(e)