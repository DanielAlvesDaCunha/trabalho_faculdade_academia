from django import forms
from django.contrib.auth.models import User

class AccountEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control bg-white rounded-4 px-3 py-2 fs-5 mb-4'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-white rounded-4 px-3 py-2 fs-5 mb-4'})
        }