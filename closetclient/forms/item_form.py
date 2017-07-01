from django import forms
from closetclient.models import Item

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('item_name', 'item_count', 'category_type', 'color')