from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.contrib import messages
from portal.decorators import check_userinfo_complete
from portal.models import UserInfo, DadosMatricula  # Certifique-se de importar o modelo Address
from portal.forms import MatriculaCreationForm
from django.urls import reverse
from django.templatetags.static import static

@method_decorator([check_userinfo_complete], name='dispatch')
class UserAddressCreateView(LoginRequiredMixin, View):
    template_name = 'dashboard/user_address_add.html'
    form_class = MatriculaCreationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        css_estilo = static('accounts/dashboard/dashboard.css')
        return render(request, self.template_name, {'form': form , 'css_estilo': css_estilo})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        css_estilo = static('accounts/dashboard/dashboard.css')
        if form.is_valid():
            user_info, created = UserInfo.objects.get_or_create(user=request.user)
            # Verifica o número de endereços já armazenados
            if DadosMatricula.objects.filter(user_info=user_info).count() < 3:
                # Salva o novo endereço aqui
                matricula = form.save(commit=False)
                matricula.user_info = user_info
                matricula.save()
                messages.success(request, 'matriculado com sucesso!')
                return redirect(reverse('user-dashboard'))
            else:
                # Mostra uma mensagem de erro se houver mais de 3 endereços
                messages.error(request, 'Você já registrou o máximo de 3 endereços.')
                return render(request, self.template_name, {'form': form})
        else:
            return render(request, self.template_name, {'form': form,'css_estilo': css_estilo})