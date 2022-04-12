# from itertools import product
# from urllib import response
from urllib import response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .basket import Basket
from store.models import *
# Create your views here.

def basket_summery(request):
    basket = Basket(request)
    context ={
        'basket':basket
    }
    return render(request, 'store/basket/basket_summery.html', context)

def basket_add(request):
    basket = Basket(request)
    # collecting the data from the ajax
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id) 
        basket.add(product=product,  qty=product_qty)
        baskettqty = basket.__len__()
        response = JsonResponse({'qty':baskettqty })
        return response
    # return render(request,'store/basket/basket_summery.html' ) 1:50:00
    
def basket_delete(request):
    basket = Basket(request)
     # collecting the data from the ajax
    if request.POST.get('action') == 'post':
         product_id = int(request.POST.get('productid'))
         basket.delete(product=product_id)
         baskettotal = basket.get_total_price()
         baskettqty = basket.__len__()
         response = JsonResponse({'qty':baskettqty, 'subtotal':baskettotal})
        #  response = JsonResponse({ 'subtotal':baskettotal}) 
         return response 
        
def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)
        
        baskettqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty':baskettqty, 'subtotal':baskettotal})
        return response