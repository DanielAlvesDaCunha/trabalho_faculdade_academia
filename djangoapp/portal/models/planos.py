# portal/models/planos.py

from django.db import models

class Plano(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.TextField()
    beneficios = models.TextField(help_text="Liste os benefícios separados por vírgula.")

    def listar_beneficios(self):
        return self.beneficios.split(',')

    def __str__(self):
        return self.nome

    def get_aluno(self):
        # Importação local para evitar o erro de importação circular
        from models import Aluno
        return Aluno.objects.all()  # Ou qualquer outra operação necessária com Aluno
