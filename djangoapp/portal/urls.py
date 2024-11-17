from django.urls import path
from .view import PlanoListView  # Certifique-se de que o arquivo esteja correto

urlpatterns = [
    path('planos/', PlanoListView.as_view(), name='plano_list'),  # URL amigável e nome padrão
]
