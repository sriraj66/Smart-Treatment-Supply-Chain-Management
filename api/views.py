from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import InputData
import json


def index(request):
    data = InputData.objects.all() 
    return render(request,'index.html',{"data":data})


@api_view(['POST'])
def receive(request):
    data = request.data
    
    model = InputData(gps=data['gps'],ecg=data['ecg'],temp=data['temp'],humid=data['humid'],gs=data['gs'],bms=data['bms'])
    model.save()

    return Response(data)