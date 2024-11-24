from functools import wraps
from django.shortcuts import redirect
from portal.models import UserInfo

def check_userinfo_complete(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        try:
            user_info = UserInfo.objects.get(user=request.user)
        except UserInfo.DoesNotExist:
            # Se não houver UserInfo, redireciona para a página de criação de UserInfo
            return redirect('portal:user-info-create')

        # Verifica se todos os campos obrigatórios foram preenchidos
        missing_fields = [field for field in ['full_name', 'cpf', 'planos', 'birthday'] if not getattr(user_info, field, None)]
        
        if missing_fields:
            # Se algum campo estiver faltando, redireciona para a página de criação de UserInfo
            return redirect('portal:user-info-create')

        # Se todos os campos estiverem completos, prossegue com a view
        return view_func(request, *args, **kwargs)

    return _wrapped_view
