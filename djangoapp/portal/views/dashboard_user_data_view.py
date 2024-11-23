from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from django.contrib import messages
from portal.decorators import check_userinfo_complete
from portal.forms import CustomUserEditForm
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static

@method_decorator([login_required, check_userinfo_complete], name='dispatch')
class UserDashboardEditView(LoginRequiredMixin, FormView):
    template_name = 'dashboard/dashboard_edit_user_data.html'
    form_class = CustomUserEditForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'instance': self.request.user})
        return kwargs

    def form_valid(self, form):
        user = form.save(commit=False)
        new_password = form.cleaned_data.get('new_password')
        if new_password:
            user.set_password(new_password)
        user.save()
        messages.success(self.request, 'Seu perfil foi atualizado com sucesso!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['css_estilo'] = static('accounts/dashboard/dashboard.css')
        return context