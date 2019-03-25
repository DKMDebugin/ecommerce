# Products urls module
from django.urls import path

from .views import (
            ProductListView,
            ProductDetailSlugView,
            )


urlpatterns = [
        path('', ProductListView.as_view(), name='list'),
        path('<str:slug>/', ProductDetailSlugView.as_view(), name='detail'),
]
