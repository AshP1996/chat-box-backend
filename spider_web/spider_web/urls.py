from django.contrib import admin
from django.urls import path, include
from web_user.views import  UserRegistrationAPIView, UserLoginAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    #for web_card app
    path('card/', include('web_card.urls')), 
    #for web_profile app
    path('user_profile/', include('web_profile.urls'))
]