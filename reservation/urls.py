from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import BookingCreate

app_name = 'reservation'

urlpatterns = [
    path('', views.home , name = "home"),
    path('room_details/<int:pk>', views.room_details , name = "room_details"),
    path('room_reserve/<int:pk>', views.room_reserve , name = "room_reserve"),
    # path('Booking/add/<class>', BookingCreate.as_view(), name="bookingcreate"),
    path('Booking/add/<int:pk>', views.BookingCreate, name="bookingcreate"),
    path('Booking/schedule/<str:pk>', views.schedule, name="schedule"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)