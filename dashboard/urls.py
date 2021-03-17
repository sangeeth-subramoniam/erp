from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'dashboard'

urlpatterns = [
    path('', views.home , name = "home"),
    path('delete/<int:pk>', views.delete , name = "delete"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)