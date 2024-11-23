from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from django.contrib import messages
from portal.models.dados_matricula import DadosMatricula
from portal.forms.matricula_forms import MatriculaCreationForm
from portal.decorators import check_userinfo_complete
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static
from django.shortcuts import get_object_or_404

@method_decorator([login_required, check_userinfo_complete], name='dispatch')
class UserAddressEditView(LoginRequiredMixin, FormView):
    template_name = 'dashboard/dashboard_edit_user_address.html'
    form_class = MatriculaCreationForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        dadosmatricula_id = self.kwargs.get('dadosmatricula_id')  # Obtém o ID do endereço da URL
        user_info = self.request.user.userinfo
        address = get_object_or_404(DadosMatricula, pk=dadosmatricula_id, user_info=user_info)
        kwargs.update({'instance': address})
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Seu endereço foi atualizado com sucesso!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(UserAddressEditView, self).get_context_data(**kwargs)
        context['css_estilo'] = static('accounts/dashboard/dashboard.css')
        return context