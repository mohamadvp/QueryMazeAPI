from django.db import models


class Product (models.Model):
    sku = models.CharField(max_length=20, primary_key=True)
    desc = models.CharField(max_length=288)
    wholesale_cost = models.DecimalField(max_digits=10, decimal_places=3)
    dims_cm = models.CharField(max_length=288)

    def __str__(self):
        return f"{self.sku} - {self.desc}"


class Customer (models.Model):
    customerid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=288)
    address = models.CharField(max_length=288)
    citystatezip = models.CharField(max_length=288)
    birthdate = models.DateField()
    phone = models.CharField(max_length=288)
    timezone = models.CharField(max_length=288)
    lat = models.FloatField()
    long = models.FloatField()

    def __str__(self):
        return self.name


class Order (models.Model):
    orderid = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ordered = models.DateTimeField()
    shipped = models.DateTimeField()
    items = models.TextField(blank=True)
    total = models.DecimalField(max_digits=20, decimal_places=3)

    def __str__(self):
         return f"Order #{self.orderid}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order , on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    unit_price = models.DecimalField(max_digits=20, decimal_places=3)

    def __str__(self):
        return f"{self.qty} x {self.product.sku} for Order #{self.order.orderid}"