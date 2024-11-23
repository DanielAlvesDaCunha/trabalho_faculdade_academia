from django.shortcuts import redirect
from django.urls import reverse
from portal.models import UserInfo

class UserInfoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # URLs que não devem ser redirecionadas
        exclude_paths = [
            reverse('portal:register'),
            reverse('portal:login'),
            reverse('portal:logout'),
            reverse('portal:user-info-create'),
        ]

        if request.user.is_authenticated:
            # Ignora redirecionamento para URLs na lista de exclusão
            if request.path not in exclude_paths:
                try:
                    user_info = UserInfo.objects.get(user=request.user)
                    # Redireciona apenas se informações obrigatórias estão faltando
                    if not user_info.full_name or not user_info.cpf or not user_info.planos:
                        return redirect('portal:user-info-create')
                except UserInfo.DoesNotExist:
                    # Redireciona se UserInfo não existe
                    return redirect('portal:user-info-create')

        return self.get_response(request)
