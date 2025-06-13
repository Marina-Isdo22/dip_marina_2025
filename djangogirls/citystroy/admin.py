from django.contrib import admin
from .models import User, Product, Order, OrderItem, CartItem, AdminAction

for model in [User, Product, CartItem, Order, OrderItem, AdminAction]:
    admin.site.register(model)


