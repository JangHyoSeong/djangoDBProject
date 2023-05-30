from django.contrib import admin
from django.urls import path, include
from main import views
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('users/',include('users.urls')),
]