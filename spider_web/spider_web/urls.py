from django.contrib import admin
from django.urls import path, include
from web_user.views import RegisterAPIView, LoginAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('user-api/', include('spider_web.urls'))
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
]
