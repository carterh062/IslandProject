from django import forms

class SearchForm(forms.Form):
    max_price = forms.CharField(label='Maximum price', max_length=100)