from django.contrib import admin
from .models import User
from .models import Product
from .models import Image
from .models import History

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(History) 