from django.contrib import admin
from .models import *

class OrderItemInline(admin.TabularInline):
  model = OrderItem

class OrderAdmin(admin.ModelAdmin):
  inlines = [
    OrderItemInline
  ]

admin.site.register(User)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
