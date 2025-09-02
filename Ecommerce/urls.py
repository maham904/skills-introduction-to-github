from django.urls import path

from myEcommerceSite.urls import urlpatterns
from . import views

urlpatterns = [
    path('mkShopping/',views.shopping_page,name = 'shopping')
]