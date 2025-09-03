from django.shortcuts import render


# Create your views here.
def shopping_page(request):
    return render(request,'shopping.html')
