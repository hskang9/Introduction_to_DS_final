from django.shortcuts import render
from django.shortcuts import HttpResponse
from recommender import *
from django.core.exceptions import *



def index(request):
    return render(request, 'base.html')


def search(request):
    if request.method == 'POST':
        query = request.POST.get('textfield', None)
        if query != None:
            sent = True
        results = recommend(query)
        del results['id']
        columns = ['Country', 'City', 'Travel Period', 'travel date', 'Price']
        return HttpResponse(results.to_html())

    else:
        return render(request, "base.html")
