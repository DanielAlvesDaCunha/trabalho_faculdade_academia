from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.contrib import messages
from portal.models import UserInfo
from portal.forms import UserInfoCreationForm

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
        try:
            # Verifique se a instância de UserInfo existe
            user_info = self.request.user.user_info
            # Verifique se todos os campos necessários estão preenchidos
            if user_info and all([user_info.full_name, user_info.cpf, user_info.planos]):
                return redirect('portal:dashboard')  # Redireciona para o dashboard se as informações estiverem completas
        except UserInfo.DoesNotExist:
            pass  # Continua no formulário de criação se não houver UserInfo ainda
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        # Salva o formulário e atualiza as informações do usuário
        user_info = form.save(commit=False)
        user_info.user = self.request.user
        user_info.save()

        # Simula o pagamento (não precisa de lógica de pagamento real)
        # Atualiza o status do pagamento ou marca o usuário como "pago"
        # Exemplo: user_info.pago = True  # Se você tivesse um campo "pago"
        user_info.save()

        # Exibe uma mensagem de sucesso e redireciona para o dashboard
        messages.success(self.request, 'Informações do usuário salvas com sucesso! Pagamento simulado.')
        print(form.errors)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
