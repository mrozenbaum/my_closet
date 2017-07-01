from django.shortcuts import render

def view_account(request):
    '''
    purpose: shows current user logged in: account_view view
    author: miriam rozenbaum
    args: request -- The full HTTP request object
    returns: render view_account view 
    '''
    template_name = 'view_account.html'
    if request.method == 'GET':
        return render(request, template_name)

    if request.method == "POST":
        return render(request, template_name)