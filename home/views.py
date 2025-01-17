from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.serializers import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from home.form import SearchForm, SignUpForm
from home.models import Setting, ContactForm, ContactFormMessage, UserProfil, FAQ
from product.models import Product, Category, ArticleForm, Article


def index(request):

    setting=Setting.objects.get(pk=1)
    sliderdata=Product.objects.all()
    category=Category.objects.all()
    products = Product.objects.all()[:6]
    dayproducts=Product.objects.all()[:4]
    lastproducts = Product.objects.all().order_by('-id')[:4]
    randomproducts = Product.objects.all().order_by('?')[:4]

    context = {'setting': setting,'category':category,
               'page':'home','sliderdata':sliderdata,
               'dayproducts':dayproducts,
               'products': products,
               'lastproducts':lastproducts,
               'randomproducts':randomproducts,}
    return render(request, 'index.html', context)

def hakkimizda(request):

    setting=Setting.objects.get(pk=1)

    context = {'setting': setting, 'page':'hakkimizda'}
    return render(request, 'hakkimizda.html', context)
def araclar(request):
    category = Category.objects.get(pk=1)
    products = Product.objects.all()
    setting=Setting.objects.get(pk=1)

    context = {'setting': setting,
               'page':'araclar',
               'category':category,
               'products':products
               }
    return render(request, 'araclar.html', context)

def referanslar(request):

    setting=Setting.objects.get(pk=1)

    context = {'setting': setting, 'page':'referanslar'}
    return render(request, 'referanslar.html', context)

def iletisim(request):

    if request.method== 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız başarı ile gönderilmiştir. Teşekkür Ederiz")
            return HttpResponseRedirect('/iletisim')

    setting=Setting.objects.get(pk=1)
    form = ContactForm()
    context = {'setting': setting, 'form':form}
    return render(request, 'iletisim.html', context)

def category_products(request,id,slug):

    setting=Setting.objects.get(pk=1)
    category = Category.objects.all()
    products=Product.objects.filter(category_id=id)

    context = {'category':category, 'products': products,'slug':slug }
    return render(request, 'products.html', context)

def product_detail(request,id,slug):
   category = Category.objects.all()
   product = Product.objects.filter(pk=id)
   context = {'products':product,'category': category}
   return render(request, 'product_detail.html',context)

def products(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            products = Product.objects.filter(title__icontains=query)
            context = { 'products': products,
                        'category': category,

                       }
            return render(request, 'products.html', context)
    return HttpResponseRedirect('/')



def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method=='POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                messages.warning(request, "login hatası! Kullanıcı adı veya şifre yanlış")
                return HttpResponseRedirect('/login')


    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'login.html', context)

def signup_view(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user=request.user
            data=UserProfil()
            data.user_id=current_user.id
            data.image="images/users/user.jpg"
            data.save()
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect('/signup')

    form =SignUpForm()
    category = Category.objects.all()
    context = {'category': category,
               'form': form,
               }
    return render(request,'signup.html',context)


def faq(request):
    category = Category.objects.all()
    faq=FAQ.objects.all().order_by('ordernumber')
    context = {'category': category,
               'faq': faq,
               }
    return render(request, 'faq.html', context)

@login_required(login_url='/login')  # Check login
def addarticle(request):
    setting = Setting.objects.get(pk=1)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)




        if form.is_valid():
            current_user = request.user
            data = Article()  # model ile bağlantı kur
            data.user_id = current_user.id
            data.category = form.cleaned_data['category']
            data.product = form.cleaned_data['product']
            data.name = form.cleaned_data['name']
            data.phone = form.cleaned_data['phone']
            data.pub_date = form.cleaned_data['pub_date']
            data.son_date = form.cleaned_data['son_date']

            data.save()
            messages.success(request, "Rezervasyon yapıldı")
            return HttpResponseRedirect('/addarticle')
        else:
            messages.success(request, 'Content Form Error:' + str(form.errors))
            return HttpResponseRedirect('/')
    else:
        category = Category.objects.all()
        form = ArticleForm()
        context = {
            'category': category,
            'form': form,
            'setting': setting,
        }
        return render(request, 'user_addproduct.html', context)

