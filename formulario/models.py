from django.db import models

class Relatorio(models.Model):
    nome = models.CharField(max_length = 100)
    data = models.DateField()
    horarioEntrada = models.TimeField()
    horarioSaida = models.TimeField()
    relatorio = models.TextField()

    def __str__(self):
        return self.nome