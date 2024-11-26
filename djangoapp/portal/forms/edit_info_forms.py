from django import forms
from portal.models import UserInfo

class UserInfoEditForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['full_name', 'cpf', 'birthday']  # Campos que podem ser editados
        widgets = {
            'birthday': forms.TextInput(attrs={'placeholder': 'dd/MM/yyyy'}),  # Exemplo de widget customizado
        }   