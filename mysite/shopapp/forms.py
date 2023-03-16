from django import forms

from .models import Product
from django.contrib.auth.models import Group


# class ProductForms(forms.Form):
#     name = forms.CharField(max_length=48)
#     price = forms.DecimalField(min_value=1, max_value=1000000, decimal_places=2)
#     description = forms.CharField(
#         label='Product discription',
#         widget=forms.Textarea(attrs={"rows": 5, "cols": 30}),
#         validators=[validators.RegexValidator(regex=r"great",
#                                               message="В поле ввода необходимо добавить слово: 'great'")],
#     )

class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "price", 'description', 'discount'


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name"]
