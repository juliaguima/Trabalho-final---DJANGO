from django import forms



class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Usuário',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs= {
                'placeholder' : 'Ex: Amanda Alves',
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


class CadastroForms(forms.Form):
        
    nome_cadastro = forms.CharField(
        label='Usuário',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs= {
                'placeholder' : 'Ex: Amanda Alves',
            }
        )
    )

    email_cadastro = forms.EmailField(
        label='Email',
        required=True,
        max_length=80,
        widget=forms.EmailInput(
            attrs= {
                'placeholder' : 'Ex: amanda@gmail.com',
            }
        )
    )

    senha_1 = forms.CharField(
        label='Senha de cadastro',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs= {
                'placeholder' : '••••••••••',
            }
        )
    )

    senha_2 = forms.CharField(
        label='Confirme a senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs= {
                'placeholder' : '••••••••••',
            }
        )
    )    