from django.urls import path
from . import views
from .views import *

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('product/<int:pk>/', views.posting, name='posting'),
    path('newProduct/', views.newProduct, name='newProduct'),
    path('wishlist/<int:pk>/', views.wishlist, name='wishlist'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)