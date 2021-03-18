from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'messaging'

urlpatterns = [
    path('', views.home , name = "home"),
    path('chat/<int:pk>', views.chat , name = "chat"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)