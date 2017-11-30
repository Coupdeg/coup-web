from django.contrib import admin
from .models import User
from .models import Product
from .models import Image
from .models import History
from .models import Cart
from .models import Item
from .models import Payment

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(History) 
admin.site.register(Cart)
admin.site.register(Item)
admin.site.register(Payment)