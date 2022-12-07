from django import forms


class NewProductForm(forms.Form):
    title = forms.CharField(max_length=55)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    slug = forms.SlugField(max_length=20)