from django import forms
from portal.models import Matricula

class MatriculaCreationForm(forms.ModelForm):
    endereco = forms.CharField(label="endereco", max_length=8, required=True)  # Corrigido
    CPF = forms.CharField(label="CPF", max_length=255, required=True)
    telefone = forms.CharField(label="telefone", max_length=10, required=True)
    
    class Meta:
        model = Matricula
        fields = ['endereco', 'CPF', 'telefone']  # Correspondente ao modelo

    def save(self, commit=True):
        matricula = super().save(commit=False)
        if commit:
            matricula.save()
        return matricula



class MatriculaEditForm(forms.ModelForm):
    endereço = forms.CharField(label="endereco", max_length=8, required=True)
    CPF = forms.CharField(label="CPF", max_length=255, required=True)
    telefone = forms.CharField(label="Telefone", max_length=10, required=True)
    
    class Meta:
        model = Matricula
        fields = ['endereco', 'CPF', 'telefone']

    def save(self, commit=True):
        matricula = super().save(commit=False)
        if commit:
            matricula.save()
        return matricula