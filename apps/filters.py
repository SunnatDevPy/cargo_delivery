import django_filters
from django_filters import NumberFilter, FilterSet, CharFilter, BooleanFilter

from apps.models import Product


class ProductFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')
    status = CharFilter(method='in_status')

    class Meta:
        model = Product
        fields = 'name',

    def in_status(self, queryset, name, value):
        qs = queryset.filter(status=value)
        return qs
