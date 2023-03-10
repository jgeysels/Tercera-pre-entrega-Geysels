from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'correo_electronico','direccion', 'telefono']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].required = True
        self.fields['apellido'].required = True
        self.fields['correo_electronico'].required = True
        self.fields['telefono'].required = True
        self.fields['direccion'].required = True
        
    def clean_correo_electronico(self):
        correo_electronico = self.cleaned_data.get('correo_electronico')
        if not correo_electronico:
            raise forms.ValidationError('Este campo es requerido.')
        if '@' not in correo_electronico:
            raise forms.ValidationError('Ingrese un correo electrónico válido.')
        return correo_electronico

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not telefono:
            raise forms.ValidationError('Este campo es requerido.')
        if len(telefono) < 8:
            raise forms.ValidationError('Ingrese un número de teléfono válido.')
        return telefono
