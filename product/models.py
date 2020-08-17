from tkinter.tix import STATUS

from django.db import models

# Create your models here.
from django.forms import ModelForm, Select, TextInput, Textarea, FileInput
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



class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    pub_date = models.DateField()

    def __str__(self):
        return self.name





class ArticleYearArchiveView(YearArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = True

class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    allow_future = True

class ArticleWeekArchiveView(WeekArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    week_format = "%W"
    allow_future = True

class ArticleDayArchiveView(DayArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    allow_future = True

class ArticleTodayArchiveView(TodayArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    allow_future = True

class Imagesw(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title
