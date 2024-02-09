from django import forms


class CreateProductForm(forms.Form):
    name = forms.CharField(min_length=1, max_length=200, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter product name'
    }))
    description = forms.CharField(min_length=0, max_length=2000, required=False, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter description'
    }))
    amount = forms.IntegerField(min_value=0, max_value=1000, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter product amount'
    }))
    price = forms.IntegerField(min_value=0, label='Price in KZT', required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter price in KZT'
    }))
