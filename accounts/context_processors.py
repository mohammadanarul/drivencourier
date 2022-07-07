from .models import Account


def user_context_processors(request):
    total_client = Account.objects.all().count()
    return {
        'total_client': total_client,
    }
