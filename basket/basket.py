from ast import Delete
from decimal import Decimal
from itertools import product
import basket
from store.models import Product


class Basket():
    """
        A BASE BASKET CLASS  providing some default behaviour that can be inherited or  over ridden, as necessay
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('session_key')
        if 'session_key' not in request.session:
            basket = self.session['session_key'] = {}
        self.basket = basket

    def add(self, product, qty):
        """
        adding and updating the session data
        """
        product_id = str(product.id)
        

        if product_id  in self.basket:
            self.basket[product_id]['qty'] =  qty
        else:
            self.basket[product_id] = {'prices': str(product.prices), 'qty': qty}
        
        

        # to save
        self.save()
        # self.session.modified = True
        

    def __iter__(self):
        """colllect the product id  in the session data to query  the data base
        and return the products
        """
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['prices'])
            item['total_price'] = item['prices'] * item['qty']
            yield item

    def __len__(self):
        """
            Get the basket data and count the quantitiy of items
        """

        return sum(item['qty'] for item in self.basket.values())

    def get_total_price(self):
        return sum(Decimal(item['prices']) * item['qty'] for item in self.basket.values())
    
    def delete(self, product):
        """
        delete item from session data
        """
        product_id = str(product)
        if product_id in self.basket:
            del self.basket[product_id]
            # self.session.modified = True
            self.save()
            
    def update(self, product, qty):
         """
         Update values in session data
         """
         product_id = str(product) 
        
         if product_id  in self.basket:
             self.basket[product_id]['qty'] = qty  
             self.save()
        
         
    def save(self):
        self.session.modified = True

        
