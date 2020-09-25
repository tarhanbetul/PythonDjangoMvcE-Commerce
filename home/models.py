from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm, Textarea, TextInput, Select

from product.models import Product


class Contact(models.Model):
    STATUS = (
        (1, 'New'),
        (2, 'Read'),
    )
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUS, default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contact Form Message"
        verbose_name_plural = "Contact Form Messages"

class ContactForm(ModelForm) :
     class Meta:
         model = Contact
         fields = ['name', 'email', 'subject', 'message']
         widgets = {
             'name'   :  TextInput(attrs={'class': 'input','placeholder':'Name & Surname'}),
             'subject' : TextInput(attrs={'class': 'input','placeholder':'Subject'}),
             'email'   : TextInput(attrs={'class': 'input', 'placeholder' :'Email Address'}),
             'message' : Textarea(attrs={'class': 'input', 'placeholder' : 'Your Message'}),

         }

