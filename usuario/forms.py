from django import forms



class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Usuário',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs= {
                'placeholder' : 'Amanda Alves',
            }
        )
    )

    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=80,
        widget=forms.PasswordInput(
            attrs= {
                'placeholder' : '••••••••••',
            }
        )
    )
