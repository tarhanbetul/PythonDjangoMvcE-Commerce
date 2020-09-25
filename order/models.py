from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput

from product.models import Product


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product =models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product

    @property
    def amount(self):
        return (self.quantity*self.product.price)




class ShopCartForm(ModelForm) :
    class Meta:
        model = ShopCart
        fields = ['quantity']
        widgets = {
            'quantity' : TextInput(attrs={'class': 'input','type':'number','value':'1'}),

        }

class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preaparing', 'Preaparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shipname =models.CharField(max_length=20)
    shipaddress =models.CharField(max_length=150)
    shipphone =models.CharField(max_length=20)
    total=models.FloatField()
    note=models.TextField()
    status =models.CharField(choices=STATUS,max_length=20,default='New')
    create_at =models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.shipname

class OrderForm(ModelForm) :
    class Meta:
        model = Order
        fields = ['shipname', 'shipaddress', 'shipphone']
        widgets = {
            'shipname': TextInput(attrs={'class': 'form-control'}),
            'shipaddress': TextInput(attrs={'class': 'form-control'}),
            'shipphone': TextInput(attrs={'class': 'form-control'}),
        }


class OrderDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price =models.FloatField()
    total =models.FloatField()
    create_at= models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product