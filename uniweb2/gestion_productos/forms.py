from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'precio']
        labels = {
            'nombre_producto': 'Nombre del Producto',
            'precio': 'Precio',
        }
        widgets = {
            'nombre_producto': forms.TextInput(attrs={
                'placeholder': 'Ej: Laptop Dell',
                'maxlength': 100,
            }),
            'precio': forms.NumberInput(attrs={
                'placeholder': 'Ej: 999.99',
                'step': '0.01',
                'min': '0',
            }),
        }

    def clean_nombre_producto(self):
        nombre = self.cleaned_data.get('nombre_producto', '').strip()
        if not nombre:
            raise forms.ValidationError('El nombre del producto no puede estar vacío.')
        return nombre

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is None or precio < 0:
            raise forms.ValidationError('El precio debe ser un valor positivo.')
        return precio
