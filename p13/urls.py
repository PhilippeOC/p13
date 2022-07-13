from django.contrib import admin
from django.urls import path, include

from oc_lettings_site import views


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('', views.home, name='home'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]
