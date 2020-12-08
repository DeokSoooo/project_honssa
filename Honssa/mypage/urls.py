from django.urls import path, include
from .views import *

app_name = 'mypage'

urlpatterns=[
    path('', mypage, name='my_main'),
    path('detail/', detail, name='my_detail'),
    path('order_list/', order_list, name='order_list'),
    path('order_list/delivery/', delivery_list, name='order_list'),]