
from django.contrib import admin

# Register your models here.
from product.models import Category, Product, Images, Article, ProductForm


class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'amount', 'image','status']

    list_filter = ['status','category']
    inlines = [ProductImageInline]

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','product', 'image']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['isim', 'arac', 'alis_tarih','iade_tarih']




admin.site.register(Article,ArticleAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images,ImagesAdmin)

