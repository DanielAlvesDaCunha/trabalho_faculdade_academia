from django import forms
from django.utils import timezone
from portal.models.avaliacao_models import Avaliacao
from portal.models.agendamento_models import Agendamento  # Importando o modelo Agendamento

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['peso', 'altura', 'aptidao']

    def clean_peso(self):
        peso = self.cleaned_data.get('peso')
        if peso is not None and peso <= 0:
            raise forms.ValidationError("O peso deve ser um valor positivo.")
        return peso

    def clean_altura(self):
        altura = self.cleaned_data.get('altura')
        if altura is not None and altura <= 0:
            raise forms.ValidationError("A altura deve ser um valor positivo.")
        return altura

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Verifica se o agendamento foi preenchido
        if not instance.agendamento:
            raise forms.ValidationError("A avaliação deve estar associada a um agendamento.")
        
        if commit:
            instance.save()
        return instance
