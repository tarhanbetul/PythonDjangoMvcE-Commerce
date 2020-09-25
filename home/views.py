from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from home.models import ContactForm, Contact
from order.models import ShopCartForm, ShopCart
from product.models import Category, Product, ProductImage

def index(request):
    catlist =Category.objects.all()
    sliderlist = Product.objects.all()[:5]
    #category = Category.objects.all()
    products = Product.objects.all()
    current_user =request.user
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()

    context = {'page': 'home',
               'catlist': catlist,
               'sliderlist': sliderlist,
               'products': products,
               }
    return render(request, 'index.html',context)

def category(request,catid):
    products =Product.objects.filter(category_id=catid)
    context = {'page': 'products',
               'products': products,
               }
    return render(request, "products.html",context)

def show_category(request,hierarchy=None):
    category_slug =hierarchy.split('/')
    category_queryset =list (Category.objects.all())
    all_slugs =[x.slug for x in category_queryset ]
    parent = None
    for slug in category_slug:
        if slug in all_slugs:
            parent = get_object_or_404(Category,slug=slug, parent=parent)
        else:
             instance =get_object_or_404(Category,slug=slug)
             breadcrumbs_link = instance.get_cat_list()
             category_name=[''.join(i.split('/')[-1].split('-')) for i in breadcrumbs_link]
             breadcrumbs =zip(breadcrumbs_link, category_name)
             return render(request,"postDetail.html", {'instance':instance, 'breadcrumbs':breadcrumbs})
    return render(request,"categories.html", {'post_set':parent.post_set.all(),'sub_categories':parent.children.all()})

def product(request,proid):

    product = Product.objects.get(pk=proid)
    images= ProductImage.objects.filter(product=proid)
    form=ShopCartForm()
    context= {'page':'products',
              'product': product,
              'images': images,
              'form':form,
              }
    return render(request,"detail.html",context)
def login_form(request):

    if request.method=="POST":
        next_url =request.POST['next']
        username =request.POST['username']
        password = request.POST['password']

        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if next_url:
                return redirect(next_url)
            else:
                HttpResponse("Home Page")
                return redirect('/')
        else:
            context = {'hata': 'Username or password incorrect',

                       }
            return render(request, "login.html",context)
    else:
        return render(request, "login.html")


def join_form(request):
    return None


def login_out(request):
    logout(request)
    return redirect('/home')

def contact_form(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():

            contactdata=Contact()
            contactdata.name = form.cleaned_data['name']
            contactdata.email = form.cleaned_data['email']
            contactdata.subject = form.cleaned_data['subject']
            contactdata.message = form.cleaned_data['message']
            contactdata.save()

            messages.success(request, "your message has been sent. Thank You for your interest ")
            return HttpResponseRedirect('/contact')
    else:
         form = ContactForm()
    return render(request, 'contact.html', {'form': form})