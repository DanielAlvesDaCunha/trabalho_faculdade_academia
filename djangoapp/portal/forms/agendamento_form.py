from django import forms
from django.utils.timezone import now, timedelta
from portal.models.agendamento_models import Agendamento

class AgendamentoForm(forms.ModelForm):
    data_horario = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label="Data e Hora",
    )

    class Meta:
        model = Agendamento
        fields = ['data_horario']

    def clean_data_horario(self):
        """Remove a validação para a data e hora, permitindo qualquer horário."""
        data_horario = self.cleaned_data['data_horario']
        
        # Remover a validação de "somente a partir de amanhã"
        return data_horario
