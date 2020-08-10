from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from home.models import Setting,ContactForm,ContactFormMessage
from product.models import Product


def index(request):

    setting=Setting.objects.get(pk=1)
    sliderdata=Product.objects.all()

    context = {'setting': setting, 'page':'home','sliderdata':sliderdata}
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