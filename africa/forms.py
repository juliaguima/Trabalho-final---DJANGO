from django import forms


class ComentarioFormsAF(forms.Form):
    Coment = forms.CharField(
        label='Comentários',
        required=True,
        max_length=5000,       
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Conte-nos a sua experiência!',
            }
        )
    )

    link_url = forms.CharField(
        widget=forms.HiddenInput()
    )