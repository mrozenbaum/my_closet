from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

# import forms and models from closetclient app
from closetclient.forms import ItemForm
from closetclient.models import Item, Category

def add_item(request):
    """
    purpose: produce a form for the User to create an item to add to their closet
    author: miriam rozenbaum
    args: request
    returns: redirect to detail view for item created
    """
    # if attempting to view, render the form.
    if request.method == 'GET':
        item_form = ItemForm()
        template_name = 'create.html'
        return render(request, template_name, {'item_form': item_form})