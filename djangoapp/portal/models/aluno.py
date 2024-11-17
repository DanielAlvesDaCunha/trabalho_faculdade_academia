from django.db import models
from .planos import Plano  # Correto, pois você está importando o modelo 'Plano' do arquivo correto 'planos.py'

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    plano = models.ForeignKey(Plano, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
