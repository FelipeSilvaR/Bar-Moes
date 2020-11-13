from django import forms


class ContactForm(forms.Form):
    nombre = forms.CharField(label="nombre", required=True, min_length=3, max_length=100, 
        widget=forms.TextInput(attrs={'class':'form-control mb-3', 'placeholder':'Ingrese su nombre'}))
    correo = forms.EmailField(label="correo", required=True, 
        widget=forms.EmailInput(attrs={'class':'form-control mb-3','placeholder':'Ingrese su correo'}))
    telefono = forms.IntegerField(label="telefono", required=True,
        widget=forms.NumberInput(attrs={'class':'form-control mb-3','placeholder':'Ingrese su teléfono'})) 
    mensaje = forms.CharField(label="mensaje", required=True, min_length=10, max_length=1000, 
        widget=forms.Textarea(attrs={'class':'form-control mb-3','placeholder':'Ingrese un comentario','rows':5}))





