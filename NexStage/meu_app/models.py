from django.db import models

class Moto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    cor = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.marca} {self.modelo}'
