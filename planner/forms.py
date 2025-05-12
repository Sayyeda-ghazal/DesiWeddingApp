# forms.py
from django import forms
from .models import Menu, QuoteRequest

class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ['name', 'email', 'phone', 'event_type', 'menu', 'guests', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3}),
        }

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'description', 'items', 'price_per_guest']