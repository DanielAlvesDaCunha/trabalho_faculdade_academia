from django.shortcuts import render
from django.views.generic import ListView

class PlanoListView(ListView):
    template_name = 'portal/plano_list.html'  # Ajuste o caminho do template conforme necessário
    context_object_name = 'planos'  # Nome do contexto para o template

    # Mova a importação para dentro da classe
    def get_queryset(self):
        from portal.models.planos import Plano  # Importação local para evitar importação circular
        return Plano.objects.all()
