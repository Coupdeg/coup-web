from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views_product as view

urlpatterns = [
		url(r'^$', view.product, name="product"),
        url(r'^(?P<product_id>[0-9]+)/$', view.detail, name="detail"),
        url(r'^(?:type=(?P<type_number>[0-6]+))/$', view.product, name="product"),
		url(r'^add_to_cart=(?P<product_id>[0-9]+)', view.add_to_cart, name="add_to_cart"),
        url(r'^remove_from_cart=(?P<product_id>[0-9]+)', view.remove_from_cart, name="remove_from_cart"),
        url(r'^update_from_cart=(?P<product_id>[0-9]+)', view.update_from_cart, name="update_from_cart"),
        url(r'^search/', view.search, name="search"),                                
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)