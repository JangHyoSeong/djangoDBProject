from django.urls import path
from . import views
from .views import *

from django.conf.urls.static import static
from django.conf import settings

app_name = 'chat'

urlpatterns = [
    path('chatroom/<int:pk>/', views.chatroom, name='chatroom'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)