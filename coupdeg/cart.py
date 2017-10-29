CART_ID = 'CART-ID'
CART = []
class Cart:
	def __init__(self):
		CART = []

	def add(self, product):
		CART.append(product)
		for p in CART: print p

	def remove(self, product):
		CART.remove(product)

	def count(self):
		return CART