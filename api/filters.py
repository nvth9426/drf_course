import django_filters
from api.models import *
from rest_framework import filters

class InStockFilterBackend(filters.BaseFilterBackend):
  def filter_queryset(self, request, queryset, view):
    return queryset.filter(stock__gt=0)
  
class ProductFilter(django_filters.FilterSet):
  name = django_filters.CharFilter(lookup_expr='iexact')

  class Meta:
    model = Product
    fields = {
      # 'name': ['exact', 'contains'],
      'name': ['iexact', 'icontains'],
      'price': ['exact', 'lt', 'gt', 'range']
    }