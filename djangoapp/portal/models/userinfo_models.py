from django.db import models

class UserInfo(models.Model):
    user = models.OneToOneField(
        'portal.CustomUser',
        on_delete=models.CASCADE,
        to_field='email',
        db_column='user_email',
        related_name='user_info_profile'
    )

    planos = (
        ('plano1',"Plano 1"),
        ('plano1',"Plano 2")
    )

    full_name = models.CharField(max_length=255,null=True)
    cpf = models.CharField(max_length=11, null=True)
    planos = models.CharField(max_length=255, choices=planos,null=True)
    birthday = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    def __str__(self):
        return self.cpf