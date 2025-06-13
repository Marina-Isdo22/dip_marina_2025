from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=10, choices=(
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    ))

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.URLField()

    def __str__(self):
        return self.name


class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.user.name} - {self.product.name}"


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateField()
    delivery_address = models.CharField(max_length=255)
    total_price = models.FloatField()
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ))

    def __str__(self):
        return f"Order #{self.id} by {self.user.name}"


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    item_price = models.FloatField()

    def __str__(self):
        return f"{self.order} - {self.product.name}"


class AdminAction(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'admin'})
    action_type = models.CharField(max_length=50)
    action_date = models.DateField()
    details = models.TextField()

    def __str__(self):
        return f"{self.admin.name} - {self.action_type}"
