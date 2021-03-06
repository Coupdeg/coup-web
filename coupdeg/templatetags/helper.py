from django import template
from ..models import Image, User
from ..cart import Cart

register = template.Library()

@register.filter
@register.simple_tag(name='index_of_product')
def index_of_product(List, i):
    return List[int(i)]

@register.filter
def index_of_image_url(i):
    image = Image.objects.filter(type_id = i)
    return image[0].image.url

@register.filter
def index_of_length(List, i):
    if len(List) < (int(i)+1):
        return False
    else:
        return True

@register.filter
def get_enum(i):
    i = str(i)
    if i == '0' :
        return "Bags"
    elif i == '1' :
        return "Soaps"
    elif i == '2' :
        return "Dresses" 
    elif i == '3' :
        return "Shirts"
    elif i == '4' :
        return "Scarves"
    elif i == '5' :
        return "Accessories"
    else :
        return "All"

@register.filter(name='times') 
def times(number):
    return range(1, number+1)

@register.filter
def cart(request):
    cart = Cart(request)
    return cart

@register.filter
def get_total_price(request):
    cart = Cart(request)
    return cart.summary()

@register.filter
def get_total_quantity(request):
    cart = Cart(request)
    return cart.count()

@register.filter
def get_role(email):
    user = User.objects.filter(email=email)
    return user[0].role

@register.filter
@register.simple_tag(name='get_user')
def get_user(email):
    user = User.objects.filter(email=email)
    return user[0]

@register.filter
def get_price_history(quantity, price):
    return quantity*price

@register.filter
def get_cart_size(cart):
    return cart.count()
                                