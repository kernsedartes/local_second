from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("homepage", views.home_again, name="homepage"),
    path("generate_qr", views.generate_qr, name="generate_qr"),
    path("qr_result", views.generate_qr, name="qr_result"),
    path("product/<uuid:uuid>/", views.product_view, name="product_view"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
