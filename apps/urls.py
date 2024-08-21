from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from apps.views import UserCreateListApiView, UserDetailApiView, ProductDetailApiView, \
    ProductCreateListApiView, LoginView
urlpatterns = [
    # user
    path('users', UserCreateListApiView.as_view(), name='users'),
    path('users/<int:pk>', UserDetailApiView.as_view(), name='user-detail'),

    # products
    path('products/<int:pk>', ProductDetailApiView.as_view(), name='product-detail'),
    path('products', ProductCreateListApiView.as_view(), name='product-create'),

    path('token', LoginView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
