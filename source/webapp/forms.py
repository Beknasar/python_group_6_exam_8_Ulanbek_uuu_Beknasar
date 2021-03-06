from django import forms
from webapp.models import Product, Review


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []


class ModerReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['status']


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['status', 'author' , 'product']