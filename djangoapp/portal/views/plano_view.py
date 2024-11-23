from django.views.generic import TemplateView

class PlanoListView(TemplateView):
    template_name = 'plano/plano_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['planos'] = [
            {'id': 1, 'nome': 'Plano Musculação', 'preco': 99.99, 'descricao': 'Plano focado em musculação', 
             'atividades': ['Musculação completa', 'Treinamento funcional']},
            {'id': 2, 'nome': 'Plano Ginástica', 'preco': 110.99, 'descricao': 'Plano focado em aulas de ginástica', 
             'atividades': ['Zumba', 'Pilates', 'Step']},
            {'id': 3, 'nome': 'Plano Artes Marciais', 'preco': 129.99, 'descricao': 'Plano focado em artes marciais', 
             'atividades': ['Muay Thai', 'Boxe', 'Jiu-Jitsu']},
        ]
        return context
