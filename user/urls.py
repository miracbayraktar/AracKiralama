from django.urls import path
from django.views.generic import ArchiveIndexView

from product.models import Article, ArticleYearArchiveView, ArticleMonthArchiveView, ArticleWeekArchiveView, \
    ArticleDayArchiveView, ArticleTodayArchiveView
from . import views

urlpatterns = [
    # ex: /product/
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
   # path('productss/', views.productss, name="productss"),
    path('addarticle/', views.addarticle, name='addarticle'),
    path('addshow/', views.addshow, name='addshow'),
    path('adddelete/', views.adddelete, name='adddelete'),
    #path('productedit/<int:id>', views.productedit, name='productedit'),
    #path('productdelete/<int:id>', views.productdelete, name='productdelete'),

    # ex: /product/5/
   # path('<int:question_id>/', views.detail, name='detail'),
    # ex: /product/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # ex: /product/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]