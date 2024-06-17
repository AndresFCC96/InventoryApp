from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
John = {"name": "John", "age": 36, "country": "Norway"}
def index(request):
    return HttpResponse("Meet John" + str(John) )