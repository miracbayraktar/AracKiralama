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
    path('addarticle/', views.addarticle, name='addarticle'),
    path('addshow/', views.addshow, name='addshow'),
    path('articledelete/<int:id>', views.articledelete, name='articledelete'),
    path('articleedit/<int:id>', views.articleedit, name='articleedit'),



]