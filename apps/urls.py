from django.contrib import admin
from django.urls import path

from apps.views import UserCreateApiView, UserListApiView, UserDetailApiView, ProductDetailApiView, \
    ProductCreateListApiView

urlpatterns = [
    # user
    path('users', UserListApiView.as_view(), name='users'),
    path('users1', UserCreateApiView.as_view(), name='user-create'),
    path('users/<int:pk>', UserDetailApiView.as_view(), name='user-detail'),

    # products
    path('products/<int:pk>', ProductDetailApiView.as_view(), name='product-detail'),
    path('products', ProductCreateListApiView.as_view(), name='product-create'),
]
