from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app/test.html')

def dados(request):
    return render(request, "app/dados.html")