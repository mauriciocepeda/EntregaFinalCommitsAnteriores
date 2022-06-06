from django import forms
from .models import Mensaje

class MensajeFormulario(forms.Form):
    message=forms.CharField(label="")

    class Meta:
        model=Mensaje
        fields=['sender','receiver','message','is_read']
