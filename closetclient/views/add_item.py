from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response


# from django.utils.datastructures import MultiValueDictKeyError

# import forms and models from closetclient app
from closetclient.forms import ItemForm
from closetclient.models import Item, Category

# def add_item(request):
#     if request.method == 'POST':
#         form = ItemForm(request.POST)
#         if form.is_valid():
#             item = form.save(commit=False)
#             item.user = request.user
#             item.save()
#             return redirect('item_details', pk=item.pk)
#         else:
#             form = ItemForm()
#         return render(request, template_name, {'item_form': item_form})
                
@login_required
def add_item(request):
    if request.POST:
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/closetclient/item_details')
        else:
        form = ItemForm()
        arg = {}
        arg.update(csrf(request))
        args['form'] = form
        return render_to_response('add_item.html', args)    
    """
    purpose: produce a form for the User to create an item to add to their closet
    author: miriam rozenbaum
    args: request
    returns: redirect to detail view for item created
    """
    # # if attempting to view, render the form.
    # if request.method == 'GET':
    #     item_form = ItemForm()
    #     template_name = 'create.html'
    #     return render(request, template_name, {'item_form': item_form})

    # if POST, gather form data and save, then redirect to details for that product
    # elif request.method == 'POST':
    #     form_data = ItemForm(request.POST)    

    #     def create_item(request):
    #         i = Item(
    #             user=request.user,
    #             item_name=form_data['item_name'],
    #             item_count=form_data['item_count'],
    #             color=form_data['color'],
    #             category_type=Category.objects.get(category_name=form_data['category_type']))
    #         if i.is_valid() and data_form.is_valid():
    #             i.save()
    #             return i
    #             form_data.save()
            
    #             return HttpResponseRedirect('/item_details')

            # return render('item_details/{}'.format(item.id))
 


