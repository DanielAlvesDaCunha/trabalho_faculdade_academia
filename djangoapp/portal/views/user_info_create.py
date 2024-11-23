from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic.edit import FormView
from django.contrib import messages
from portal.models import UserInfo
from portal.forms import UserInfoCreationForm
from django.templatetags.static import static

class UserInfoCreateView(LoginRequiredMixin, FormView):
    template_name = 'registration/user_info_create.html'
    form_class = UserInfoCreationForm
    success_url = '/portal/dashboard/'  # Redireciona para o dashboard após o preenchimento

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user_info, created = UserInfo.objects.get_or_create(user=self.request.user)
        kwargs.update({'instance': user_info})
        return kwargs

    def get(self, request, *args, **kwargs):
        # Verifique se o usuário já possui informações associadas antes de renderizar o formulário
        if self.request.user.user_info and self.request.user.user_info.full_name and self.request.user.user_info.cpf and self.request.user.user_info.planos:
            return redirect('portal:dashboard')  # Se as informações já estão preenchidas, redireciona para o dashboard
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        # Aqui você pode integrar o pagamento ou outras lógicas, como validações adicionais
        user_info = form.save()
        self.request.user.user_info = user_info  # Vincula o UserInfo ao usuário
        self.request.user.save()

        # Simulando um pagamento bem-sucedido, você pode adicionar sua lógica de pagamento aqui
        if user_info.planos and user_info.full_name and user_info.cpf:  # Exemplo de verificação
            messages.success(self.request, 'Informações do usuário e pagamento processados com sucesso!')
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Erro ao processar as informações ou pagamento. Tente novamente.')
            return redirect('portal:user-info-create')  # Redireciona para a página de criação de informações caso algo falhe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['css_estilo'] = static('accounts/dashboard/user_info.css')
        return context
