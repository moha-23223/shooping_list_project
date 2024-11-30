from django import forms
from .models import Product, shoppinglist


class productform(forms.ModelForm):
  class Meta:
    model = Product
    fields = ['name',  'price']

class Shoppingform(forms.ModelForm):
  class Meta:
    model = shoppinglist
    fields = ['id_product', 'amount', 'id_user']

  def __init__(self, *args, **kwargs):
    self.id_user = kwargs.pop('id_user', None)
    super().__init__(*args, **kwargs)

  def save(self, commit=True):
    instance = super().save(commit=False)
    if self.id_user:
      instance.id_user = self.id_user
    if commit:
      instance.save()
    return instance  