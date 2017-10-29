CART_ID = 'CART-ID'
class Cart:
	def __init__(self, request):
		
		self.CART = []

	def add(self, product):
		self.CART.append(product)
		for p in self.CART: print p

	def remove(self, product):
		self.CART.remove(product)

	def count(self):
		return self.CART