from rest_framework.viewsets import ModelViewSet
from carreras.models import Carrera
from carreras.api.serializers import CarreraSerializer
from rest_framework.exceptions import PermissionDenied

class CarreraApiViewSet(ModelViewSet):
    serializer_class = CarreraSerializer
    queryset = Carrera.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_staff:
                return Carrera.objects.all()
            return Carrera.objects.filter(driver=user)
        # Manejo del caso en que el usuario no está autenticado
        else:
            raise PermissionDenied({"message": "Debes estar autenticado para ver las carreras"})
            # return Carrera.objects.none()  # Devuelve un QuerySet vacío