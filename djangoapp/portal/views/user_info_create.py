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
        try:
            # Verifique se a instância de UserInfo existe
            user_info = self.request.user.user_info
            if user_info:  # Verifique se a instância não é None
                if all([user_info.full_name, user_info.cpf, user_info.planos]):
                    return redirect('portal:dashboard')  # Redireciona para o dashboard
        except UserInfo.DoesNotExist:
            pass  # Continua no formulário de criação se não houver UserInfo ainda
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        # Salva o formulário e atualiza as informações do usuário
        user_info = form.save(commit=False)
        user_info.user = self.request.user
        user_info.save()

        # Verifica se o formulário está completo
        if user_info.planos and user_info.full_name and user_info.cpf:
            messages.success(self.request, 'Informações do usuário salvas com sucesso!')
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Preencha todas as informações obrigatórias.')
            return redirect('portal:user-info-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context