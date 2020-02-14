from django.contrib import admin
from .models import Item, Itemlast, Itemforu, OrderItem, Order, Join

# Register your models here.
admin.site.register(Item)
admin.site.register(Itemlast)
admin.site.register(Itemforu)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Join)