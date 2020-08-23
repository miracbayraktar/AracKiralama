from tkinter.tix import STATUS

from django.db import models

# Create your models here.
from django.db.models import DateField
from django.forms import ModelForm, Select, TextInput, Textarea, FileInput, DateInput
from django.urls import reverse
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from django.views.generic import YearArchiveView, MonthArchiveView, WeekArchiveView, DayArchiveView, TodayArchiveView


class Category(models.Model):

    STATUS=(
        ('True','Evet'),
        ('False','Hayır'),
    )

    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    status=models.CharField(max_length=10, choices=STATUS)
    slug=models.SlugField()
    parent=models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Product(models.Model):
        STATUS = (
            ('True', 'Evet'),
            ('False', 'Hayır'),
        )

        category = models.ForeignKey(Category, on_delete=models.CASCADE)
        title = models.CharField(max_length=130)
        keywords = models.CharField(max_length=255)
        description = models.CharField(max_length=255)
        image = models.ImageField(blank=True, upload_to='images/')
        price=models.FloatField()
        amount=models.IntegerField()
        detail=RichTextUploadingField()

        status = models.CharField(max_length=10, choices=STATUS)
        create_at = models.DateTimeField(auto_now_add=True)
        update_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.title


class Images(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'title', 'keywords', 'description', 'image','status']
        widgets = {
            'category': Select(attrs={'class': 'input', 'placeholder': 'amount'}, choices={Category.objects.all()}),
            'title': TextInput(attrs={'class': 'input', 'placeholder': 'title'}),
            'keywords': TextInput(attrs={'class': 'input', 'placeholder': 'keywords'}),
            'description': Textarea(attrs={'class': 'input', 'placeholder': 'description'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image'}),
            'status': Select(attrs={'class': 'input', 'placeholder': 'status'}, choices=STATUS),


        }





class Imagesw(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

class Article(models.Model):

    arac = models.ForeignKey(Product, on_delete=models.CASCADE)
    isim = models.CharField(max_length=30)
    telefon = models.CharField(max_length=12)
    alis_tarih = models.DateField()
    iade_tarih = models.DateField()


    def __str__(self):
        return self.isim

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = [ 'arac', 'isim', 'telefon','alis_tarih','iade_tarih']
        widgets = {

            'arac': Select(attrs={'class': 'input', 'placeholder': 'araç'}, choices={Product.objects.all()}),
            'isim': TextInput(attrs={'class': 'input', 'placeholder': 'isim'}),
            'telefon': TextInput(attrs={'class': 'input', 'placeholder': 'telefon'}),
            'alis_tarih':DateInput(attrs={'class': 'input', 'placeholder': 'alıs_tarihi'}),
            'iade_tarih': DateInput(attrs={'class': 'input', 'placeholder': 'iade_tarihi'}),

        }





class ArticleYearArchiveView(YearArchiveView):
    queryset = Article.objects.all()
    date_field = "alis_tarih"
    date_fields = "iade_tarih"
    make_object_list = True
    allow_future = True

class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Article.objects.all()
    date_field = "alis_tarih"
    date_fields = "iade_tarih"
    allow_future = True

class ArticleWeekArchiveView(WeekArchiveView):
    queryset = Article.objects.all()
    date_field = "alis_tarih"
    date_fields = "iade_tarih"
    week_format = "%W"
    allow_future = True

class ArticleDayArchiveView(DayArchiveView):
    queryset = Article.objects.all()
    date_field = "alis_tarih"
    date_fields = "iade_tarih"
    allow_future = True

class ArticleTodayArchiveView(TodayArchiveView):
    queryset = Article.objects.all()
    date_field = "alis_tarih"
    date_fields = "iade_tarih"
    allow_future = True