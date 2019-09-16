from django.shortcuts import render
from django.http import JsonResponse
from andch_back_app.models import Client

# Create your views here.

def all_clients(request):
    clients = Client.objects.all()
    clientList = []
    for client in clients:
        clientList.append({'clientName': client.clientName, 'imagePath': client.imagePath},)
    data = {'clients' : clientList}

    return JsonResponse(data)