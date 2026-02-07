"""
URL configuration for projetHotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include


def api_root(request):
    """Page d'accueil de l'API."""
    return JsonResponse({
        "message": "API Hotel - Bienvenue",
        "endpoints": {
            "admin": "/admin/",
            "users": "/api/users/",
            "hotels": "/api/hotels/",
            "password_reset": "/api/password_reset/",
        },
    })


urlpatterns = [
    path('', api_root),
    path('admin/', admin.site.urls),
    path('api/', include('hotell.urls')),
    path('api/users/', include('users.urls')),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]

