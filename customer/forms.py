from .models import Customer
from django.forms import ModelForm, TextInput, NumberInput, Textarea

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname','lastname','age','profession']

        widgets = {
            "firstname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Fristname'
            }),
            "lastname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Lastname'
            }),
            "age": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Age'
            }),
            "profession": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Profession'
            }),
        }