from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from portal.decorators import check_userinfo_complete
from portal.models import CustomUser, UserInfo, DadosMatricula
from django.contrib.auth.decorators import login_required

@method_decorator([login_required, check_userinfo_complete], name='dispatch')
class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

    # Obtendo usuário customizado
        custom_user = get_object_or_404(CustomUser, pk=self.request.user.pk)

    # Recuperando UserInfo ou redirecionando
        try:
            user_info = UserInfo.objects.get(user=self.request.user)
        except UserInfo.DoesNotExist:
            return redirect('portal:user-info-create')

    # Filtrando DadosMatricula usando user_info.user (CustomUser)
        custom_address = DadosMatricula.objects.filter(user_info=user_info.user).order_by('created_at')
        address_count = custom_address.count()

    # Adicionando ao contexto
        context.update({
        'custom_user': custom_user,
        'user_info': user_info,
        'custom_address': custom_address,
        'address_count': address_count,
    })

        return context
