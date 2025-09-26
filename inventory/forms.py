from django.forms import ModelForm
from .models import *
    
class Product_Form(ModelForm):
     class Meta:
        model = Product 
        fields = "__all__"

class Customer_Form(ModelForm):
     class Meta:
        model = Customers 
        fields = "__all__"

class Order_Form(ModelForm):
     
     class Meta:
        model = Orders 
        fields = ['product_reference','customer_reference','order_date','order_number','quantity']
