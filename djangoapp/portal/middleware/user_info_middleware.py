from django.shortcuts import redirect
from django.urls import reverse
from portal.models import UserInfo

class UserInfoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Resolver as URLs dinamicamente com namespace correto
        exclude_paths = [
            reverse('portal:register'),
            reverse('portal:login'),
            reverse('portal:logout'),
            reverse('portal:user-info-create'),  # Incluído o namespace
            reverse('portal:dashboard'),
        ]

        if request.user.is_authenticated:
            # Verificar se a URL atual não está nas excluídas
            if request.path not in exclude_paths:
                try:
                    user_info = UserInfo.objects.get(user=request.user)
                    # Redirecionar se informações estiverem incompletas
                    if not all([user_info.full_name, user_info.cpf, user_info.planos]):
                        return redirect('portal:user-info-create')  # Incluído o namespace
                except UserInfo.DoesNotExist:
                    # Redirecionar se o UserInfo não existir
                    return redirect('portal:user-info-create')  # Incluído o namespace

        return self.get_response(request)
