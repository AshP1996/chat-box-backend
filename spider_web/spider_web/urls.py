from django.contrib import admin
from django.urls import path, include
from web_user.views import  UserRegistrationAPIView, UserLoginAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('card/', include('web_card.urls')), 
]