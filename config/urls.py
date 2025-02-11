"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # allauth
    path('accounts/', include('allauth.urls')),

    # local urls
    path('', include('ogani.apps.products.urls', namespace='products')),
    path('carts/', include('ogani.apps.carts.urls', namespace='carts')),
    path('contacts/', include('ogani.apps.contacts.urls', namespace='contacts')),
    path('blog/', include('ogani.apps.blog.urls', namespace='blog')),
    path('profile/', include('ogani.apps.accounts.urls', namespace='accounts')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # /media/user/user.png
