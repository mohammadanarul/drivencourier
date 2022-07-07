from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
UserModel = get_user_model()


class EmailOrPhoneNumberBackend(ModelBackend):
    def authenticate(self, request, phone_number=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(phone_number__iexact=phone_number) | Q(email__iexact=phone_number))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
            return
        except UserModel.MultipleObjectsReturned:
            user = UserModel.objects.filter(Q(phone_number__iexact=phone_number) | Q(email__iexact=phone_number)).order_by('id').first()

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
