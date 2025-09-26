from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    product_code=models.CharField(max_length=50, unique=True)
    gst=models.IntegerField(default=0)

    def __str__(self):
        return self.name + " - " + self.product_code 
    
class Customers(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField(max_length=100, unique=True)
    age=models.IntegerField(default=0)
    Address=models.CharField(max_length=50, unique=True)
    Phone=models.IntegerField(default=0)

    def __str__(self):
        return self.name + " - " + self.email
    
class Orders(models.Model):
    product_reference = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_reference = models.ForeignKey(Customers, on_delete=models.CASCADE)
    order_date = models.DateField(null=True)
    order_number=models.CharField(max_length=50)
    quantity = models.IntegerField(default=1)
    amount=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    gst_amount=models.IntegerField(default=0)
    bill_amount=models.DecimalField(max_digits=10, decimal_places=2, default=0)


    def __str__(self):
        return f"Order of {self.quantity} {self.product.name}(s) by {self.customer.name} on {self.order_date} and {self.order_number}"
