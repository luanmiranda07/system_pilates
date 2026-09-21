from rest_framework.routers import DefaultRouter
from apps.agenda.views import AulaViewSet

router = DefaultRouter()
router.register(r"aulas", AulaViewSet)

urlpatterns = router.urls