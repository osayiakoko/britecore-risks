from rest_framework.routers import DefaultRouter
from .views import RiskTypeViewSet


app_name = 'v1'

router = DefaultRouter()
router.register(r'risktypes', RiskTypeViewSet, basename='risktype')
urlpatterns = router.urls
