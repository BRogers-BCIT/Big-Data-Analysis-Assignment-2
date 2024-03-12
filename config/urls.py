"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/

Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

Added home and results pages.
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('pages.urls')),
    path('', include('pages.urls'))
]
