from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.filters import ProductFilter
from apps.models import User, Product
from apps.serializers import UserModelSerializer, ProductModelSerializer


@extend_schema(tags=['User'])
class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


@extend_schema(tags=['User'])
class UserCreateListApiView(ListCreateAPIView):
    queryset = User.objects.all()


@extend_schema(tags=['User'])
class UserDetailApiView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


@extend_schema(tags=['Product'])
# SearchFilter
class ProductCreateListApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    filter_backends = DjangoFilterBackend,
    filterset_class = ProductFilter

    def get_serializer(self, *args, **kwargs):
        kwargs.setdefault('context', self.get_serializer_context())
        return ProductModelSerializer(*args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


@extend_schema(tags=['Product'])
class ProductDetailApiView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()

    def get_serializer(self, *args, **kwargs):
        kwargs.setdefault('context', self.get_serializer_context())
        return ProductModelSerializer(*args, **kwargs)

    def get_queryset(self):
        if self.request.user.role != 'admin':
            return super().get_queryset().filter(owner=self.request.user)
        return super().get_queryset().all()


@extend_schema(tags=['Auth'])
class LoginView(TokenObtainPairView):
    pass


@extend_schema(tags=['Auth'])
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
