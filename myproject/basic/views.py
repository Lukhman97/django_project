from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.

data={
    'name':"Virat Kholi",
    'age':38,
    'city':"Ranchi",
    'country':"India"
}
def wish(request):
    return HttpResponse("HELLO WORLD")


def greet(request):
    return HttpResponse("WElCOME TO DJANGO.......")

def details(request):
    return JsonResponse(data)

def sampleinfo(request):
    data1={'resukt':[12,33,4445,556,66666]}
    return JsonResponse(data1 | data)
