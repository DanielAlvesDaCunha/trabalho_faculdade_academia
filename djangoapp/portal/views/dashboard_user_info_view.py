from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from django.contrib import messages
from portal.decorators import check_userinfo_complete
from portal.models import UserInfo
from portal.forms import UserInfoEditForm
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static

@method_decorator([login_required, check_userinfo_complete], name='dispatch')
class UserInfoDashboardEditView(LoginRequiredMixin, FormView):
    template_name = 'dashboard/dashboard_edit_user_info.html'
    form_class = UserInfoEditForm
    success_url = '/' 

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user_info, created = UserInfo.objects.get_or_create(user=self.request.user)
        kwargs.update({'instance': user_info})
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Informações do usuário atualizadas com sucesso!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['css_estilo'] = static('accounts/dashboard/user_info.css')
        context['css_estilo2'] = static('accounts/dashboard/dashboard.css')
        return context