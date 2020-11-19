from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
# Create your views here.
def index(request):
    if 'term' in request.GET:
        print('True')
        qs = Product.objects.filter(title__istartswith=request.GET.get('term'))
        titles = list()
        for product in qs:
            titles.append(product.title)
        return JsonResponse(titles, safe=False)
    return render(request, 'searchform/index.html',{ 'liste': ['java', 'c++', 'js']})