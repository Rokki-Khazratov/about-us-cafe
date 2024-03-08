from django import forms
from .models import Aplication

class AplicationForm(forms.ModelForm):
    class Meta : 
        model = Aplication
        fields = ['full_name','phone_number','job']

    full_name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number= forms.IntegerField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    cost = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    job = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(choices=Aplication.APLICATION_CHOISES_FIELD, widget=forms.Select(attrs={'class': 'form-control'}))