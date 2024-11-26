from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from django.contrib import messages
from portal.decorators import check_userinfo_complete
from portal.models import UserInfo
from portal.forms import UserInfoEditForm
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from django.templatetags.static import static
from django.shortcuts import redirect
from portal.models import UserInfo
from portal.forms import UserInfoEditForm
from portal.decorators import check_userinfo_complete

@method_decorator([login_required, check_userinfo_complete], name='dispatch')
class UserInfoEditView(LoginRequiredMixin, FormView):
    template_name = 'dashboard/dashboard_edit_info.html'  # Template que será usado para exibir o formulário
    form_class = UserInfoEditForm  # Formulário que será renderizado
    success_url = reverse_lazy('portal:dashboard')  # Redireciona para o dashboard ou outra página após sucesso

    # Passando a instância de UserInfo para o formulário
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user_info, created = UserInfo.objects.get_or_create(user=self.request.user)  # Recupera ou cria o UserInfo
        kwargs.update({'instance': user_info})  # Passa a instância para o formulário
        return kwargs

    # Método chamado quando o formulário é válido e enviado
    def form_valid(self, form):
        form.save()  # Salva as alterações no banco de dados
        messages.success(self.request, 'Informações do usuário atualizadas com sucesso!')
        return super().form_valid(form)  # Redireciona com sucesso

    # Passando context adicional para o template, se necessário
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['css_estilo'] = static('accounts/dashboard/user_info.css')  # CSS personalizado
        context['css_estilo2'] = static('accounts/dashboard/dashboard.css')  # CSS adicional
        return context