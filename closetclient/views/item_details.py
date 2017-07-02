from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

# import forms and models from closetclient app
from closetclient.models import Item

def item_details(request, category_id):
    """
    purpose: allows User to view item_detail view, which contains a specific view for a single item
    author: miriam rozenbaum
    args: item_id: (integer): id of item we are viewing
    returns: (render): a view of the request, template to use, and item obj
    """
    # If trying to view, render item corresponding to id passed

    template_name = 'details.html'
    category = get_object_or_404(Category, pk=category_id)
    items = Item.objects.filter(category_type=category).exclude(quantity=0)
    # display items        
    return render(request, template_name, {
        'category': category,
        'items': items})            



