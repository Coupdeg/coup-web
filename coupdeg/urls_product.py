from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views_product as view

urlpatterns = [
		url(r'^$', view.product, name="product"),
        url(r'^(?P<product_id>[0-9]+)/$', view.details, name="details")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)