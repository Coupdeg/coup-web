CART_ID = 'CART-ID'
CART = []
class Cart:
	def __init__(self, request):
		self.cart = self.new(request)

	def new(self, request):
		request.session[CART_ID] = 0
		return '1'

	def add(self, product):
		CART.append(product)
		print(len(CART))
		return '0'

	def remove(self, request):
		return '-1'