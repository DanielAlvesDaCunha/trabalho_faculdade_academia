from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy  # Certifique-se de que essa importação está correta
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from django.contrib import messages
from portal.forms.edit_conta_forms import AccountEditForm
from portal.decorators import check_userinfo_complete
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static

@method_decorator([login_required, check_userinfo_complete], name='dispatch')
class UserContaView(LoginRequiredMixin, FormView):
    template_name = 'dashboard/dashboard_edit_conta.html'  # Template a ser utilizado
    form_class = AccountEditForm  # Formulário de edição de conta
    success_url = reverse_lazy('portal:dashboard')  # Redirecionamento para a página do dashboard após sucesso

    # Passando o usuário logado para o formulário
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'instance': self.request.user})  # Atualizando a instância com o usuário logado
        return kwargs

    # Lógica para salvar as alterações do formulário
    def form_valid(self, form):
        user = form.save(commit=False)
        new_password = form.cleaned_data.get('new_password')
        if new_password:
            user.set_password(new_password)  # Se a senha foi alterada, atualiza
        user.save()  # Salva as mudanças no banco de dados
        messages.success(self.request, 'Seu perfil foi atualizado com sucesso!')  # Mensagem de sucesso
        return super().form_valid(form)

    # Passando contexto adicional para o template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['css_estilo'] = static('accounts/dashboard/dashboard.css')  # Estilo CSS
        return context