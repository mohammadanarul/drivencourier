from django.shortcuts import render


def about_view(request):
    return render(request, 'about.html')


def handle_bad_request(request, exception):
    context = {
        'title': '400 Not available this page.',
        'status': 400,
    }
    return render(request, 'exception_handling/exception-handle.html', context, status=400)


def handle_permission_denied(request, exception):
    context = {
        'title': '403 Forbidden.',
        'status': 403,
    }
    return render(request, 'exception_handling/exception-handle.html', context, status=403)


def handle_page_not_found(request, exception):
    print(exception)
    context = {
        'title': '404 Not Found this page.',
        'status': 404,
    }
    return render(request, 'exception_handling/exception-handle.html', context, status=404)


def handle_server_error(request):
    context = {
        'title': 'Not Service 500.',
        'status': 500,
    }
    return render(request, 'exception_handling/exception-handle.html', context, status=500)
