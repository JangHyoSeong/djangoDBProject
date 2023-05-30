from django.contrib import admin
from django.urls import path, include
from main import views as main_views
from users import views as users_views
from chat import views as chat_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('users/',include('users.urls')),
    path('chat/', include('chat.urls')),
]