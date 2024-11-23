# portal/models/plano.py
from django.db import models

class Plano(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.TextField()
    atividades = models.TextField()  # Lista de atividades separada por vírgulas
    
    class Meta:
        abstract = True  # Torna esse modelo abstrato, sem tabela no banco de dados

    def listar_atividades(self):
        return self.atividades.split(',')

    def __str__(self):
        return self.nome
from django.db import models
from .plano import Plano 

class PlanoMusculacao(Plano):
    atividades_adicionais = models.TextField()  # Atividades específicas para o plano de musculação

    def __str__(self):
        return f"Plano de Musculação: {self.nome}"

class PlanoGinastica(Plano):
    atividades_adicionais = models.TextField()  # Atividades específicas para o plano de ginástica

    def __str__(self):
        return f"Plano de Ginástica: {self.nome}"

class PlanoArtesMarciais(Plano):
    atividades_adicionais = models.TextField()  # Atividades específicas para o plano de artes marciais

    def __str__(self):
        return f"Plano de Artes Marciais: {self.nome}"