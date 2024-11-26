from django.db import models
from django.conf import settings
from django.utils import timezone
from portal.models.agendamento_models import Agendamento

class Avaliacao(models.Model):
    aluno = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='avaliacoes')
    agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE, related_name='avaliacoes')
    data_horario = models.DateTimeField(default=timezone.now)
    disponivel = models.BooleanField(default=True)
    peso = models.FloatField(null=True, blank=True)
    altura = models.FloatField(null=True, blank=True)
    aptidao = models.TextField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.aluno.username} - {self.data_horario}"

