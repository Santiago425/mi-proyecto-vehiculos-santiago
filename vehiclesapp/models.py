from django.db import models

class vehicle(models.Model):
    placa = models.CharField(max_length=20)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)

    COLOR_CHOICES = [
        ('rojo', 'Rojo'),
        ('azul', 'Azul'),
        ('negro', 'Negro'),
        ('blanco', 'Blanco'),
        ('gris', 'Gris'),
    ]

    color_vehiculo = models.CharField(
        max_length=20,
        choices=COLOR_CHOICES,
        default='negro'
    )

    def __str__(self):
        return self.placa
