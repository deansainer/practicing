from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.index, name='home_page_url'),
    path('product_list/', views.product_list, name='product_list_url'),
    path('product/<str:slug>/', views.product_details, name='product_details_url'),
    path('new_product/', NewProductView.as_view(), name='new_product_url'),
]