from django.db import models

PLANOS_CHOICES = (
    ('plano1', "Plano 1"),
    ('plano2', "Plano 2")
)

class UserInfo(models.Model):
    user = models.OneToOneField(
        'portal.CustomUser',
        on_delete=models.CASCADE,
        to_field='email',  # Use apenas se for necessário
        db_column='user_email',  # Use apenas se precisar no banco
        related_name='user_info_profile'
    )
    full_name = models.CharField(max_length=255, null=True)
    cpf = models.CharField(max_length=11, unique=True, null=True)
    planos = models.CharField(max_length=255, choices=PLANOS_CHOICES, null=True)
    birthday = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name or f"Usuário sem nome ({self.user.email})"