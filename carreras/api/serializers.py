from rest_framework import serializers
# from rest_framework.serializers import ModelSerializer
from carreras.models import Carrera

class CarreraSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    driver = serializers.StringRelatedField()
    
    class Meta:
        model = Carrera
        fields = ['id', 'origen', 'destino', 'fecha_hora', 'status', 'status_display', 'driver']