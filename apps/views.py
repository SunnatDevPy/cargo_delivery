from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, ListAPIView

from apps.filters import ProductFilter
# from apps.filters import ProductFilter
from apps.models import User, Product
from apps.serializers import UserModelSerializer, ProductModelSerializer


# Create your views here.
class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    # def get_serializer(self, *args, **kwargs):
    #     kwargs.setdefault('context', self.get_serializer_context())
    #     return UserModelSerializer(*args, **kwargs)


class UserCreateListApiView(ListCreateAPIView):
    queryset = User.objects.all()


class UserDetailApiView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


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


class ProductDetailApiView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()

    def get_serializer(self, *args, **kwargs):
        kwargs.setdefault('context', self.get_serializer_context())
        return ProductModelSerializer(*args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)
