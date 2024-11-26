from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from portal.forms.avaliacao_forms import AvaliacaoForm
from portal.models.avaliacao_models import Avaliacao
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


from django.shortcuts import redirect

class AvaliacaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Avaliacao
    form_class = AvaliacaoForm
    template_name = 'portal/avaliacao_form.html'

    def get_success_url(self):
        return reverse_lazy('portal:cria-avaliacao')

    def get_object(self, queryset=None):
        try:
            return Avaliacao.objects.get(aluno=self.request.user)
        except Avaliacao.DoesNotExist:
        # Redireciona para a criação da avaliação, caso não exista
            return redirect('portal:criar_avaliacao')