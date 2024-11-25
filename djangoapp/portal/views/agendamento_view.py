from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from portal.models.agendamento_models import Agendamento

class AgendamentoCreateView(CreateView):
    model = Agendamento
    fields = ['data_horario']  # Apenas o campo que o aluno escolhe
    template_name = 'portal/agendamento_form.html'
    success_url = reverse_lazy('agendamento_sucesso')

    def form_valid(self, form):
        # Adiciona o aluno logado ao agendamento
        form.instance.aluno = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtro de datas indisponíveis
        form.fields['data_horario'].queryset = Agendamento.objects.filter(disponivel=True)
        return form
