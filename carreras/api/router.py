from rest_framework.routers import DefaultRouter
from carreras.api.views import CarreraApiViewSet

router_carreras = DefaultRouter()
router_carreras.register(
    prefix='carreras', basename='carreras', viewset=CarreraApiViewSet
)