from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from order.models import ShopCartForm, ShopCart


def index(request):
    return HttpResponse("order app")

@login_required(login_url='/login')
def addtocart(request,id):
    url=request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form=ShopCartForm(request.POST)
        if form.is_valid():
            current_user=request.user

            data=ShopCart()
            data.user_id=current_user.id
            data.product_id=id
            data.quantity=form.cleaned_data['quantity']
            data.save()

            messages.success(request,"Araç başarıyla sepete eklenmiştir")

            return HttpResponseRedirect(url)

    if id:
        current_user = request.user
        data = ShopCart()
        data.user_id = current_user.id
        data.product_id = id
        data.quantity =1
        data.save()
        messages.success(request, "Araç başarıyla sepete eklenmiştir")

        return HttpResponseRedirect(url)

    messages.warning(request,"hata oluştu")
    return HttpResponseRedirect(url)