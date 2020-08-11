from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from home.models import Setting,ContactForm,ContactFormMessage
from product.models import Product, Category


def index(request):

    setting=Setting.objects.get(pk=1)
    sliderdata=Product.objects.all()
    category=Category.objects.all()
    dayproducts=Product.objects.all()
    lastproducts = Product.objects.all().order_by('-id')
    randomproducts = Product.objects.all().order_by('?')

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