"""proje URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.postgres import search
from django.urls import path, include

from home import views

urlpatterns = [
    path('', include('home.urls')),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('araclar/', views.araclar, name='araclar'),
    path('referanslar/', views.referanslar, name='referanslar'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('home/', include('home.urls')),
    path('product/', include('product.urls')),
    path('user/', include('user.urls')),
    path('order/', include('order.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('category/<int:id>/<slug:slug>/', views.category_products, name='category_products'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/', views.products, name='products'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/',views.login_view,name='login_view'),
    path('signup/',views.signup_view,name='signup_view'),
    path('sss/',views.faq,name='faq'),

    path('user/',views.UserProfil, name='user'),







]
if settings.DEBUG: # new
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)