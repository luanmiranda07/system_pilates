
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/token/", TokenObtainPairView.as_view()),
    path("api/v1/token/refresh/", TokenRefreshView.as_view()),
    path("api/v1/", include("apps.clientes.urls")),
    path("api/v1/", include("apps.professores.urls")),
    path("api/v1/", include("apps.agenda.urls")),
]
