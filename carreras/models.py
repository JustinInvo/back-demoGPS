from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Carrera(models.Model):

    ESTADOS = [
        ('PL', 'Planificada'),
        ('EP', 'En Proceso'),
        ('CO', 'Completada'),
    ]

    origen = models.CharField(max_length=200)
    destino = models.CharField(max_length=200)
    fecha_hora = models.DateTimeField()
    status = models.CharField(
        max_length=2,
        choices=ESTADOS,
        default='PL',
    )
    driver = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.destino
