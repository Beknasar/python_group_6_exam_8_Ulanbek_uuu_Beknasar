from django import forms
from webapp.models import Product, Review


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']