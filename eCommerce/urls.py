"""eCommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

from .views import Home, home, About, contact, login_page, register_page, logout_view


urlpatterns = [
    path('cart/', include(('carts.urls', 'cart'), 'cart')),
    # path('tags/', include(('tags.urls', 'tags'), 'tags')),
    path('search/', include(('search.urls', 'search'), 'search')),
    path('products/', include(('products.urls', 'products'), 'products')),
    path('contact/', contact, name='contact'),
    path('about/', About.as_view(), name='about'),
    path('bootstrap/', TemplateView.as_view(template_name='example/bootstrap.html')),
    path('', home, name='home'),
    # path('', Home.as_view(), name='home'),
    path('register/', register_page, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_page, name='login'),
    path('admin/', admin.site.urls),

]

# url to static files in a non production env
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
