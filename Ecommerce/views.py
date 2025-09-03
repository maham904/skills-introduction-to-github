from django.shortcuts import render


# Create your views here.
def shopping_page(request):
    return render(request,'shopping.html')

def cart_page(request):
    return render(request, 'cart.html')

def payment_page(request):
    return render(request, 'payment.html')
