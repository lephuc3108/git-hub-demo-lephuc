from django.contrib import admin
from .models import Item, OrderItem, Order, Blogpost, Categories

# Register your models here.
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Blogpost)
admin.site.register(Categories)