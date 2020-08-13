from django.urls import path

from . import views

urlpatterns = [
    # ex: /product/
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),


    # ex: /product/5/
   # path('<int:question_id>/', views.detail, name='detail'),
    # ex: /product/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # ex: /product/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]