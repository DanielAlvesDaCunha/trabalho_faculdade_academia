from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from portal.models.agendamento_models import Agendamento

class AvaliacaoUpdateView(UpdateView):
    model = Agendamento
    fields = ['peso', 'altura', 'aptidao']
    template_name = 'portal/avaliacao_form.html'
    success_url = reverse_lazy('avaliacao_sucesso')

    def get_queryset(self):
        return Agendamento.objects.filter(disponivel=True, peso__isnull=True)