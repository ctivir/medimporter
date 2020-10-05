from django.shortcuts import render
from django.http import HttpResponse

from .models import Produto

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'index.html')

def search(request):
    """A view of all bands."""
    produtos = Produto.objects.all()
    return render(request, 'index.html', {'produtos': produtos})