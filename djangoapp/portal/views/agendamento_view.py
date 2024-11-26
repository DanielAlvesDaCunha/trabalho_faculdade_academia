from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.urls import reverse
from portal.forms.agendamento_form import AgendamentoForm
from portal.models.agendamento_models import Agendamento

class AgendamentoCreateView(CreateView):
    model = Agendamento
    form_class = AgendamentoForm    
    template_name = 'agendamento/agendamento_form.html'

    def form_valid(self, form):
        # Adiciona o aluno logado ao agendamento
        form.instance.aluno = self.request.user
        agendamento = form.save()

        # Redireciona para a avaliação após criar o agendamento, passando o 'pk' da avaliação ou agendamento
        return HttpResponseRedirect(reverse('portal:criar-avaliacao'))


