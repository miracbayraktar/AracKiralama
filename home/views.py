from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from home.form import SearchForm, SignUpForm
from home.models import Setting, ContactForm, ContactFormMessage, UserProfil
from product.models import Product, Category


def index(request):

    setting=Setting.objects.get(pk=1)
    sliderdata=Product.objects.all()
    category=Category.objects.all()
    dayproducts=Product.objects.all()[:4]
    lastproducts = Product.objects.all().order_by('-id')[:4]
    randomproducts = Product.objects.all().order_by('?')[:4]

    context = {'setting': setting,'category':category, 'page':'home','sliderdata':sliderdata,'dayproducts':dayproducts,'lastproducts':lastproducts,'randomproducts':randomproducts,}
    return render(request, 'index.html', context)

def hakkimizda(request):

    setting=Setting.objects.get(pk=1)

    context = {'setting': setting, 'page':'hakkimizda'}
    return render(request, 'hakkimizda.html', context)

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

def product_search(request):

    if request.method== 'POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query=form.cleaned_data['query']
            product = Product.objects.filter(title__icontains='query')
            context = {'products': product, 'category': category}
            return render(request, 'products_search.html', context)

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