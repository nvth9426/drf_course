import django_filters
from api.models import *

class ProductFilter(django_filters.FilterSet):
  name = django_filters.CharFilter(lookup_expr='iexact')

  class Meta:
    model = Product
    fields = {
      # 'name': ['exact', 'contains'],
      'name': ['iexact', 'icontains'],
      'price': ['exact', 'lt', 'gt', 'range']
    }