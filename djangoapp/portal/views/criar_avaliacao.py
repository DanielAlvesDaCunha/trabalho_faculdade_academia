from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from portal.models.agendamento_models import Agendamento
from portal.forms.avaliacao_forms import AvaliacaoForm
from portal.models.avaliacao_models import Avaliacao

class CriarAvaliacaoView(CreateView):
    model = Avaliacao
    form_class = AvaliacaoForm
    template_name = 'agendamento/criar_avaliacao_form.html'
    success_url = reverse_lazy('portal:dashboard')

    def form_valid(self, form):
        # Encontrar um agendamento ativo para o aluno logado
        agendamento = Agendamento.objects.filter(aluno=self.request.user, disponivel=True).first()

        if agendamento:
            # Se o agendamento ativo existir, associar à avaliação
            form.instance.agendamento = agendamento
        else:
            # Caso não haja agendamento ativo, adicionar um erro e retornar
            form.add_error(None, "Você precisa de um agendamento ativo para criar uma avaliação.")
            return self.form_invalid(form)

        # Salvar a avaliação associada ao agendamento
        form.instance.aluno = self.request.user  # Associando o aluno logado
        form.save()

        return redirect(self.success_url)

    def get_success_url(self):
        return reverse_lazy('portal:dashboard')