class Product:
    "This class describes a product. Add commit"
    
    def __init__ (self, name: str, price:float) -> None:
        self.name = name
        self.price = price
    def calc_product_total(self, quantity):
        return self.price*quantity

class ShoppingCart():
    "This class describes a product"
    cart = {}
    total = 0

    def add_to_cart(self, product: Product, quantity: int):
        if self.cart.get(product):
            self.cart[product] += quantity
        else:
            self.cart[product] = quantity
    def calc_total(self):
        # print(self.cart)
        for p in self.cart:
            self.total += p.calc_product_total(self.cart[p])


apple = Product("apple",10)
orange = Product("orange",50)
cart = ShoppingCart()
cart.add_to_cart(orange,2)
cart.add_to_cart(apple,10)
cart.calc_total()

print(cart.total)



