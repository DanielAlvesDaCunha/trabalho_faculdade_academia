# from django.http import Http404
# from django.shortcuts import redirect, render, get_object_or_404
# from django.urls import reverse_lazy
# from django.views.generic import FormView
# from portal.forms.matricula_form import MatriculaForm

# class MatriculaView(FormView):
#     form_class = MatriculaForm
#     template_name = 'matricula/matricula.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         aluno_id = self.kwargs.get('id')  # Pega o id do aluno da URL
#         print(f"Recebido aluno_id: {aluno_id}")  # Depuração para ver o id recebido

#         try:
#             aluno_profile = get_object_or_404(AlunoProfile, user__id=aluno_id)
#             print(f"Aluno encontrado: {aluno_profile}")
#         except AlunoProfile.DoesNotExist:
#             print(f"AlunoProfile não encontrado para o id: {aluno_id}")
#             raise Http404("AlunoProfile não encontrado")

#         context['aluno'] = aluno_profile
#         context['plano'] = aluno_profile.plano
#         context['atividades'] = aluno_profile.plano.beneficios.split(',')  # Exemplo de atividades
#         return context