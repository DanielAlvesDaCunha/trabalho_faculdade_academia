from django import forms

from portal.models.userinfo_models import UserInfo


class UserInfoCreationForm(forms.ModelForm):
    full_name = forms.CharField(label="Nome completo", max_length=100, required=True)
    email = forms.CharField(label="E-mail", required=True)
    planos = forms.ChoiceField(label='Planos', choices=[('plano1', 'Musculação, R$119,99'), ('plano2', 'Artes Marciais, R$119,99'), ('plano3', 'Ginastica, R$119,99'), ('plano4', 'Musculação,Artes Marciais e Ginastica, R$199,99')], required=True)
    birthday = forms.DateField(label='Data de nascimento', help_text="Formato: DD/MM/YYYY")
    cpf = forms.CharField(label="CPF", required=True)  # Adicionando CPF

    class Meta:
        model = UserInfo
        fields = ['full_name', 'email', 'planos', 'birthday', 'cpf']  # Incluindo CPF

    def save(self, commit=True):
        user_info = super().save(commit=False)
        if commit:
            user_info.save()
        return user_info


class UserInfoEditForm(forms.ModelForm):
    full_name = forms.CharField(label="Nome completo",max_length=100, required=True)
    email = forms.CharField(label="email", required=True)
    planos = forms.ChoiceField(label='planos',choices=[('plano1', 'Musculação, R$119,99'), ('plano2', 'Artes Marciais, R$119,99'), ('plano3', 'Ginastica, R$119,99')])
    birthday = forms.DateField(label='Data de nascimento',help_text="Formato: DD/MM/YYYY")
    cpf = forms.CharField(label="CPF", required=True)  # Adicionando CPF


    class Meta:
        model = UserInfo
        fields = ['full_name', 'email', 'planos', 'birthday', 'cpf']  # Incluindo CPF

    def save(self, commit=True):
        user_info = super().save(commit=False)
        if commit:
            user_info.save()
        return user_info