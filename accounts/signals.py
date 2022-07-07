import random
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Account, Merchant, Rider
from .thread import SendAccountActivationEmail


@receiver(post_save, sender=Account)
def send_email_token(sender, instance, created, **kwargs):
    try:
        if not instance.otp:
            otp = str(random.randint(100000, 999999))
            title = 'Congratulations Email activation Code.'
            instance.otp = otp
            ''' EXCEUTING THREAD TO SEND EMAIL '''
            print('I am a main accounts signals', otp, instance.email)
            SendAccountActivationEmail(instance.email, otp, title).start()

    except Exception as e:
        print(e)


@receiver(post_save, sender=Rider)
def send_email_token(sender, instance, created, **kwargs):
    try:
        if not instance.otp:
            otp = str(random.randint(100000, 999999))
            title = 'Congratulations Email activation Code.'
            instance.otp = otp
            instance.save()
            ''' EXCEUTING THREAD TO SEND EMAIL '''
            print('I am a rider signals', otp, instance.email)
            SendAccountActivationEmail(instance.email, otp, title).start()

    except Exception as e:
        print(e)


@receiver(post_save, sender=Merchant)
def send_email_token(sender, instance, created, **kwargs):
    try:
        if not instance.otp:
            otp = str(random.randint(100000, 999999))
            title = 'Congratulations Email activation Code.'
            instance.otp = otp
            instance.save()
            ''' EXCEUTING THREAD TO SEND EMAIL '''
            print('I am a merchant signals', otp, instance.email)
            SendAccountActivationEmail(instance.email, otp, title).start()

    except Exception as e:
        print(e)
