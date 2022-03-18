from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def handle_bad_request(request, exception):
    context = {
        'title': '400 Not avilalbe this page.',
    }
    return render(request, 'exception_handling/exception-handle.html', context, status=400)


def handle_permission_denied(request, exception):
    context = {
        'title': '403 Forbidden.',
    }
    return render(request, 'exception_handling/exception-handle.html', context, status=403)

def handle_page_not_found(request, exception):
    print(exception)
    context = {
        'title': '404 Not Found this page.',
    }
    return render(request, 'exception_handling/exception-handle.html', context, status=404)


def handle_server_error(request):
    context = {
        'title': 'Not Service 500.',
    }
    return render(request, 'exception_handling/exception-handle.html', context, status=500)
