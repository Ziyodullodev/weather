from django.shortcuts import render
from django.http import JsonResponse
from .getweather import getweather
# Create your views here.

# def WeatherView(request):
#     getdata = getweather()
#     data = {
#         "Bugun":getdata
#     }
#     return JsonResponse(data)