from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views_user as views

urlpatterns = [
    url(r'^register/', views.register, name="register"),
    url(r'^login/', views.login, name="login"),
    url(r'^history/', views.history, name="history"),
	url(r'^$', views.user, name="user"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)