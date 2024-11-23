from django import forms
from django.contrib.auth.forms import UserCreationForm
from portal.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email',)

class CustomUserEditForm(forms.ModelForm):
    new_password = forms.CharField(label='Nova Senha', widget=forms.PasswordInput(), required=False)
    confirm_password = forms.CharField(label='Confirmar Nova Senha', widget=forms.PasswordInput(), required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password and new_password != confirm_password:
            self.add_error('confirm_password', 'A nova senha e a confirmação não correspondem.')

        return cleaned_data