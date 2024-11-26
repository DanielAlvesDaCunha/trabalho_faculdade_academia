from django.db import models
from django.conf import settings  # Importando settings para usar AUTH_USER_MODEL

class Agendamento(models.Model):
    aluno = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='agendamentos')
    data_horario = models.DateTimeField()
    disponivel = models.BooleanField(default=True)  # Usado para verificar a disponibilidade
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.aluno.username} - {self.data_horario}"