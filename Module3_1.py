# !/usr/bin/env python
# -*- coding: utf-8 -*-

class Product:
    "This class describes a product"
    def __init__ (self, name: str, price: float) -> None:
        self.name = name
        self.price = price
    def calc_product_total(self, quantity):
        return float(self.price*quantity)

class ShoppingCart():
    """This class describes a ShoppingCart

    Attributes
    __________
    cart : list
    quantity_cart: list

    Methods
    __________
    add_to_cart(self, product: Product, quantity: int)
        Adds a product to the cart and adds the quantity to the quantity_cart

    calc_total(self)
        Calculates the total price of all products added to the cart
    """

    cart = []
    quantity_cart = []

    def add_to_cart(self, product: Product, quantity: int):
        """Adds  a product to the cart and adds the quantity to the quantity_cart."""
        self.cart.append(product)
        self.quantity_cart.append(quantity)


    def calc_total(self):
        """Calculates the total price of all products added to the cart."""
        total = 0
        for p in range(len(self.cart)):
            total += self.cart[p].calc_product_total(self.quantity_cart[p])
        return total



apple = Product("apple",30)
apple_2 = Product("apple",30)
orange = Product("orange",50)
cart_1 = ShoppingCart()
cart_1.add_to_cart(orange,4)
cart_1.add_to_cart(apple,2)
cart_1.add_to_cart(apple_2,1)
print(cart_1.cart)
print(cart_1.quantity_cart)

print(cart_1.calc_total())

