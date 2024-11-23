
from django.db import models

class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    plano = models.CharField(max_length=100)
    aluno = models.CharField(max_length=100)

    def __str__(self):
        return self.nome