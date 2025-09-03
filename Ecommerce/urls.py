from django.urls import path
from . import views

urlpatterns = [
    path('mkShopping/',views.shopping_page,name = 'shopping'),
    path('cart/', views.cart_page, name='cart'),
    path('payment/', views.payment_page, name='payment'),
]