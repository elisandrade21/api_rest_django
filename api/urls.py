from django.contrib import admin
from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token

from .api import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/login/', obtain_jwt_token),
    path('api/v1/', include(router.urls))
]
