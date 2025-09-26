from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages

def HomePage(request):

     data={
          'name': "Inventory Management System",
          'version': '1.0',
          'author': 'admins',
          'description': 'A simple inventory management system.' ,
          'features': ['Add items', 'View items', 'Update items', 'Delete items'],
          'technologies': ['Django', 'SQLite', 'HTML', 'CSS', 'JavaScript'],
     }

     return render(request, 'home.html',data)

def ServicesPage(request):
    return render(request, 'services.html')

def ContactPage(request):
    return render(request, 'contact.html')

def AboutPage(request):
    return render(request, 'about.html')

def Product_add(request):

    context={'product_form':Product_Form(),}

    if request.method=="POST":
        product_form=Product_Form(request.POST)
        if product_form.is_valid():
            product_form.save()
            context['success_message']="Product added successfully!"
        
    return render(request, 'product_add.html',context)

def Product_view(request):

    contex={'all_products' :Product.objects.all()}
    return render(request, 'products.html',contex)

def delete_product(request, id):
    selected_product = Product.objects.get(id=id)
    selected_product.delete()
    messages.success(request, "Product deleted successfully!")
    return redirect('/inventory/product_view/')

def product_update(request, id):


    selected_product = Product.objects.get(id=id)
    product_form = Product_Form(instance=selected_product)
    context = {'product_form': product_form, 'product_id': id}
    if request.method == "POST":
        product_form = Product_Form(request.POST, instance=selected_product)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, "products updated successfully!")
            return redirect('/inventory/product_view/')
         


    return render(request, 'product_add.html', context)

def Customer_add(request):

    context={'customer_form':Customer_Form(),}

    if request.method=="POST":
        customer_form=Customer_Form(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            context['success_message']="Customer added successfully!"
        
    return render(request, 'customer_add.html',context)

def Customer_view(request):

    contex={'all_customers' :Customers.objects.all()}
    return render(request, 'customer_view.html',contex)

def delete_customer(request, id):
    selected_customer = Customers.objects.get(id=id)
    selected_customer.delete()
    messages.success(request, "Customer deleted successfully!")
    return redirect('/inventory/customer_view/')

def customer_update(request, id):


    selected_customer = Customers.objects.get(id=id)
    customer_form = Customer_Form(instance=selected_customer)
    context = {'customer_form': customer_form, 'customer_id': id}
    if request.method == "POST":
        customer_form = Customer_Form(request.POST, instance=selected_customer)
        if customer_form.is_valid():
            customer_form.save()
            messages.success(request, "Customer updated successfully!")
            return redirect('/inventory/customer_view/')
    return render(request, 'customer_add.html', context)
    
def Orders_add(request):

    context={'order_form':Order_Form(),}

    if request.method == "POST":
    
        selected_product = Product.objects.get(id=request.POST['product_reference'])
        amount=selected_product.price * int(request.POST.get('quantity'))
        gst_amount=(amount * selected_product.gst)/100
        bill_amount=amount + gst_amount
        new_orders = Orders(
            customer_reference_id = request.POST['customer_reference'],
            product_reference_id = request.POST['product_reference'],
            order_date=request.POST['order_date'],
            order_number=request.POST['order_number'],  
            quantity=request.POST['quantity'],
            amount=amount,
            gst_amount=gst_amount,
            bill_amount=bill_amount)
        new_orders.save()
            
        
    
    return render(request, 'orders_add.html',context)

def Orders_view(request):

    contex={'all_orders' :Orders.objects.all()}
    return render(request, 'orders_details.html',contex)

def delete_order(request, id):
    selected_order = Orders.objects.get(id=id)
    selected_order.delete()
    messages.success(request, "Order deleted successfully!")
    return redirect('/inventory/orders_view/')

def order_update(request, id):


    selected_order = Orders.objects.get(id=id)
    order_form = Order_Form(instance=selected_order)
    context = {'order_form': order_form, 'order_id': id}
    if request.method == "POST":
        selected_product = Product.objects.get(id=request.POST['product_reference'])
        amount=selected_product.price * int(request.POST.get('quantity'))
        gst_amount=(amount * selected_product.gst)/100
        bill_amount=amount + gst_amount
        order_form = Order_Form(request.POST, instance=selected_order)
        if order_form.is_valid():
            updated_order = order_form.save(commit=False)
            updated_order.amount = amount
            updated_order.gst_amount = gst_amount
            updated_order.bill_amount = bill_amount
            updated_order.save()
            messages.success(request, "Order updated successfully!")
            return redirect('/inventory/orders_view/')
         


    return render(request, 'orders_add.html', context)
