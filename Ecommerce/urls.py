from django.urls import path
from . import views

urlpatterns = [
    path('mkShopping/',views.shopping_page,name = 'shopping')
]