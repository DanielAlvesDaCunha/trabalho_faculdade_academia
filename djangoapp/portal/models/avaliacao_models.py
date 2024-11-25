from portal import models
from django.contrib.auth.models import User


class Agendamento(models.Model):
    aluno = models.ForeignKey(User, on_delete=models.CASCADE, related_name='agendamentos')
    data_horario = models.DateTimeField()
    disponivel = models.BooleanField(default=True)
    peso = models.FloatField(null=True, blank=True)
    altura = models.FloatField(null=True, blank=True)
    aptidao = models.TextField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.aluno.username} - {self.data_horario}"
