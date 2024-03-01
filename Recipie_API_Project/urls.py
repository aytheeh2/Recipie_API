from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as Rviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('API.urls')),
    path('token/', Rviews.obtain_auth_token),
]
