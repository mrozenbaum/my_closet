from django import forms
from closetclient.models import Item, Category

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('item_name', 'item_count', 'color', 'category_type')