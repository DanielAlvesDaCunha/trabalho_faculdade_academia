from django.db import models

from django.contrib.auth.models import User

from project import settings  # ou outro modelo que represente o usuário

class DadosMatricula(models.Model):
    user_info = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True)
    cpf = models.CharField(max_length=11, null = True)
    peso = models.FloatField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    