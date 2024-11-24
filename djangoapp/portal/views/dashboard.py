from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from portal.decorators import check_userinfo_complete
from portal.models import CustomUser, UserInfo, DadosMatricula
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static

@method_decorator([login_required, check_userinfo_complete], name='dispatch')
class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        custom_user = get_object_or_404(CustomUser, pk=self.request.user.pk)
        
        try:
            user_info = UserInfo.objects.get(user=self.request.user)
        except UserInfo.DoesNotExist:
            # Caso o user_info não exista, você pode redirecionar ou mostrar uma mensagem de erro
            return redirect('portal:user-info-create')  # Exemplo de redirecionamento para criar info

        custom_address = DadosMatricula.objects.filter(user_info=user_info).order_by('created_at')
        address_count = custom_address.count()
        
        dadosmatricula_id = self.request.GET.get('dadosmatricula_id')
        
        context['custom_user'] = custom_user
        context['user_info'] = user_info
        context['dadosmatriculaid'] = dadosmatricula_id
        context['custom_address'] = custom_address
        context['address_count'] = address_count
        context['css_estilo'] = static('accounts/dashboard/dashboard.css')
        
        return context
