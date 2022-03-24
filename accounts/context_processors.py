from .models import Account

def user_context_processors(request):
    total_cliend = Account.objects.all().count()
    return {
        'total_cliend': total_cliend,
    }