from django.shortcuts import render

from closetclient.models import Category
from django.http import HttpResponse

# Create your views here.

def categories(request):
    if request.method == 'GET':
        template_name = 'categories.html'
        try:
            latest_category_list = Category.objects.order_by('category_name')    
            return render(request, template_name, {
                  'latest_category_list': latest_category_list})
        except TypeError:
            return render(request, template_name, {
                  'latest_category_list': list('apple')})