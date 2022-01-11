from django.urls import path
from .views import *

urlpatterns = [
    path('', CustomerList.as_view(), name='customer_list_url'),
    path('customer/<str:slug>', GeneratePdfDetails.as_view(), name='customer_detail'),

    path('create/', CustomerCreate.as_view(), name='customer_create'),
    path('update/<str:slug>/', CustomerUpdate.as_view(), name='customer_update'),
    path('<str:slug>', CustomerFront.as_view(), name='customer_front'),
    path('delete/<str:slug>/', CustomerDelete.as_view(), name='customer_delete'),

]
