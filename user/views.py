from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from home.models import UserProfil, Setting
from product.models import Category, Product, ProductForm
from user.forms import UserUpdateForm, ProfileUpdateForm


def index(request):
    category = Category.objects.all()
    current_user=request.user
    profile=UserProfil.objects.get(user_id=current_user.id)
    context = {'category': category,'profile': profile}
    return render(request, 'user_profile.html',context)


def user_update(request):
    if request.method=='POST':
        user_form=UserUpdateForm(request.POST, instance=request.user)
        profile_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofil)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'güncellendi')
            return  redirect('/user')

    else:
        category=Category.objects.all()
        current_user=request.user
        user_form=UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=request.user.userprofil)
        context = {'category': category,
                   'user_form': user_form,
                   'profile_form': profile_form
        }
        return render(request, 'user_update.html',context)


def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'password değişti')
            return  redirect('change_password')
        else:
            messages.error(request, 'Lütfen doğru şifre girin.<br>'+ str(form.errors))
            return HttpResponseRedirect('/user/password')

    else:
        category=Category.objects.all()

        form=PasswordChangeForm(request.user)
        context ={'form': form,'category': category}


        return render(request, 'change_password.html',context)

@login_required(login_url='/login')  # Check login
def productss(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    current_user = request.user
    productss= Product.objects.filter(user_id=current_user.id, status='True')
    context = {
        'category': category,
        'productss': productss,
        'setting': setting,
    }
    return render(request, 'user_productss.html', context)

@login_required(login_url='/login')  # Check login
def addproduct(request):
    setting = Setting.objects.get(pk=1)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)




        if form.is_valid():
            current_user = request.user
            data = Product()  # model ile bağlantı kur
            data.user_id = current_user.id
            data.category = form.cleaned_data['category']
            data.address = form.cleaned_data['address']
            data.title = form.cleaned_data['title']
            data.keywords = form.cleaned_data['keywords']
            data.description = form.cleaned_data['description']
            data.image = form.cleaned_data['image']

            data.slug = form.cleaned_data['slug']
            data.status = 'False'

            data.save()
            messages.success(request, "Başarılı bir şekilde eklendi..")
            return HttpResponseRedirect('/user/productss/')
        else:
            messages.success(request, 'Content Form Error:' + str(form.errors))
            return HttpResponseRedirect('/')
    else:
        category = Category.objects.all()
        form = ProductForm()
        context = {
            'category': category,
            'form': form,
            'setting': setting,
        }
        return render(request, 'user_addproduct.html', context)

@login_required(login_url='/login')  # Check login
def productedit(request, id):
    setting = Setting.objects.get(pk=1)
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'İlan Başarıyla Güncellenmiştir !')
            return HttpResponseRedirect('/user/productss/')
        else:
            messages.success(request, 'mekan Form Error: ' + str(form.errors))
            return HttpResponseRedirect('/user/productedit/' + str(id))
    else:
        category = Category.objects.all()
        form = ProductForm(instance=product)
        context = {
            'category': category,
            'form': form,
            'setting': setting,
        }
        return render(request, 'user_addproduct.html', context)


@login_required(login_url='/login')  # Check login
def productdelete(request, id):
    current_user = request.user
    Product.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'İlan Silindi..')
    return HttpResponseRedirect('/user/productss/')


