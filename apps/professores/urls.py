from rest_framework.routers import DefaultRouter
from apps.professores.views import ProfessoresViewSet

router = DefaultRouter()
router.register(r"professores", ProfessoresViewSet, basename="professores")

urlpatterns = router.urls