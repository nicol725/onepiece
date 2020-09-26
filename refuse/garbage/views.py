from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from garbage import models

data={}
def details(request):
    data['detail'] = models.Refuse.objects.all().values()
    return render(request,"details.html",data)

def get(request):
    if request.method == 'GET':
        cityName = request.GET.get('city')
        # refuse = models.Refuse.objects.get(city=cityName).values()
        refuse = serializers.serialize("json", models.Refuse.objects.filter(city=cityName))
        # print(refuse)
        return HttpResponse(refuse)
    return HttpResponse("123")

def index(request):
    data['detail'] = models.Refuse.objects.all().values()
    return render(request, "index.html", data)