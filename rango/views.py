from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {
        'boldmessage': 'Crunchy, cream, cookie, candy, cupcake'
    }
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return HttpResponse("Rango says here is the about page.")
