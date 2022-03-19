from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from helpers.views import AboutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls', namespace='accounts')),
    path('', include('percels.urls', namespace="percels")),
    path('pickup/', include('pickuplocations.urls', namespace="pickuplocations")),
    path('about/', AboutView.as_view(), name='about_view')
]

# exception handling view
handler400 = 'helpers.views.handle_bad_request'
handler403 = 'helpers.views.handle_permission_denied'
handler404 = 'helpers.views.handle_page_not_found'
handler500 = 'helpers.views.handle_server_error'

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
