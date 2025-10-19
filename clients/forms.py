from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'cash', 'hawa', 'note']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم العميل'}),
            'cash': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'كاش'}),
            'hawa': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'هوا'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'ملاحظات', 'rows': 2}),
        }
