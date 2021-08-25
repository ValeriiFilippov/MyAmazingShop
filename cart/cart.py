from shop.models import Product
from django.conf import settings
from decimal import Decimal


class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.SESSION_ID_CART)
        if not cart:
            cart = self.session[settings.SESSION_ID_CART] = {}
        self.cart = cart

    def add(self, product: Product, count: int = 1, update_count: bool = False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'count': 0,
                                     'price': str(product.price)}

        if update_count:
            self.cart[product_id]['count'] = count
        else:
            self.cart[product_id]['count'] += count
        self.save()

    def remove(self, product: Product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session[settings.SESSION_ID_CART] = self.cart
        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['count'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.SESSION_ID_CART]
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['count']
            yield item

    def __len__(self):
        return sum(item['count'] for item in self.cart.values())


