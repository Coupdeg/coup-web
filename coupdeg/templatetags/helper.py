from django import template
register = template.Library()

@register.filter
def index_of_product_name(List, i):
    return List[int(i)].name

@register.filter
def index_of_image_url(List, i):
    return List[int(i)].image.url

@register.filter
def index_of_length(List, i):
    if len(List) < (int(i)+1):
        return False
    else:
        return True