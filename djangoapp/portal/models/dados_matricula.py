from django.db import models

# from portal.models.userinfo_models import UserInfo

class DadosMatricula(models.Model):
    # user_info = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=8)
    peso = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
