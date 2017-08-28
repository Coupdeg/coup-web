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