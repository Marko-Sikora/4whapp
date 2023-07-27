from django import forms 
from .models import zamowienia

class zamowienia_forma(forms.ModelForm):
    class Meta:
        model = zamowienia
        fields ='__all__'
        