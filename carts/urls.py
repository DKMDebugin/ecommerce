"""Carts app urls module"""

from django.urls import path

from .views import (
                    cart_home,
                    cart_update,
                    # cart_remove
                    )

urlpatterns = [

        path('', cart_home, name='home'),
        path('update/', cart_update, name='update'),
        # path('remove/', cart_remove, name='remove'),
]
