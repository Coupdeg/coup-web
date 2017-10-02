from django import template
register = template.Library()

@register.filter
@register.simple_tag(name='index_of_product')
def index_of_product(List, i):
    return List[int(i)]

@register.filter
def index_of_image_url(List, i):
    return List[int(i)].image.url

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