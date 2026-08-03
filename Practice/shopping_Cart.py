from discount_system import *
from product import *


class ShoppingCart:
    def __init__(self):
        self._items = {}
        self._discount = None

    def add_item(self, product: Product, quantity:int = 1):
        self._items[product] = quantity


    def remove_item(self, product_id:str):
        for product in list(self._items.keys()):
            if product.product_id == product_id:
                del self._items[product]

    def apply_discount(self, discount):


    def calculate_subtotal(self):
        subtotal = 0.0
        for product, quantity in self._items.items():
            subtotal += product.price * quantity
        return subtotal

    def calculate_shipping(self):
        for product in self._items.keys():
            product.get_shipping_cost()

    def calculate_total(self):
        total = self.calculate_subtotal() -

