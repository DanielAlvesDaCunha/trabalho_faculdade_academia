# from django import forms
# from portal.models import AlunoProfile, Plano, Matricula  # Ajuste conforme necessário

# class MatriculaForm(forms.ModelForm):
#     plano = forms.ModelChoiceField(queryset=Plano.objects.all(), label='Escolha o Plano')  # Campo de escolha de plano
#     atividades = forms.CharField(widget=forms.Textarea, required=False, disabled=True)  # Atividades associadas ao plano
#     cpf = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'placeholder': 'Digite o CPF'}), label='CPF')
#     cep_residencia = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Digite o CEP'}), label='CEP de Residência')

#     class Meta:
#         model = Matricula  # Ou o modelo de aluno que você está usando
#         fields = ['plano', 'atividades', 'cpf', 'cep_residencia']

#     def __init__(self, *args, **kwargs):
#         super(MatriculaForm, self).__init__(*args, **kwargs)
#         if self.instance.pk:  # Se for uma edição, mostrar as atividades associadas ao plano
#             self.fields['atividades'].initial = ', '.join(self.instance.plano.atividades.split(','))  # Caso tenha atividades no plano
