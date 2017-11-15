from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views_admin as views

urlpatterns = [
    url(r'^$', views.index, name="admin"),
    url(r'^add-product/', views.add_product, name="add-product"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)