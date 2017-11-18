from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views_admin as views

urlpatterns = [
    url(r'^$', views.index, name="admin"),
    url(r'^product/add', views.add_product, name="add-product"),
    url(r'^product/show', views.show_product, name="show-product"),
    url(r'^product/delete', views.delete_product, name="delete-product"),                            
    url(r'^product/edit/(?P<product_id>[0-9]+)/$', views.edit_product, name="edit-product"),                        
    url(r'^product/', views.product, name="admin-product"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)