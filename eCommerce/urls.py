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

from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from django.conf.urls import url

from accounts.views import LoginView, guest_register_view, RegisterView
from addresses.views import checkout_address_create_view, checkout_address_reuse_view
from carts.views import cart_detail_api_view
from .views import Home, home, About, contact



urlpatterns = [

    path('cart/', include(('carts.urls', 'cart'), 'cart')),
    path('products/', include(('products.urls', 'products'), 'products')),
    path('search/', include(('search.urls', 'search'), 'search')),

    path('', home, name='home'),
    # path('', Home.as_view(), name='home'),
    path('api/cart/', cart_detail_api_view, name='api-cart'),
    path('checkout/address/create/', checkout_address_create_view, name='checkout_address_create'),
    path('checkout/address/reuse/', checkout_address_reuse_view, name='checkout_address_reuse'),
    path('contact/', contact, name='contact'),
    path('bootstrap/', TemplateView.as_view(template_name='example/bootstrap.html')),
    path('about/', About.as_view(), name='about'),

    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/guest/', guest_register_view, name='guest_register'),
    path('admin/', admin.site.urls),

]

# url to static files in a non production env
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
