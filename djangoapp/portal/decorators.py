from functools import wraps
from django.shortcuts import redirect
from portal.models import UserInfo

def check_userinfo_complete(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user_info = UserInfo.objects.filter(user=request.user).first()
        if user_info is None:
            return redirect('user-info-create')
        missing_fields = [field for field in ['full_name', 'cpf', 'plano', 'birthday'] if getattr(user_info, field, None) is None]
        if missing_fields:
            return redirect('user-info-create')
        return view_func(request, *args, **kwargs)
    return _wrapped_view