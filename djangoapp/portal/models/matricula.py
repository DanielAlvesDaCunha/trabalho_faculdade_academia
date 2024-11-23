# portal/models/matricula.py
from django.db import models
from .plano import PlanoMusculacao  # Pode escolher qualquer um dos planos derivados

class Matricula(models.Model):
    plano = models.ForeignKey(PlanoMusculacao, on_delete=models.CASCADE, related_name='matriculas')
    endereco = models.CharField(max_length=255)
    aluno = models.CharField(max_length=100)
    data_matricula = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('ativo', 'Ativo'), ('cancelado', 'Cancelado')],
        default='ativo'
    )
    cpf = models.CharField(max_length=14)

    def __str__(self):
        return f"Matricula do aluno no plano {self.plano.nome}"
