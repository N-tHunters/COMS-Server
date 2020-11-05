from django.shortcuts import render
from COMSAPI.models import Client


# Create your views here.
def index(request):
    bar_status = False
    computers_connected = Client.objects.count()
    computers_online = Client.objects.filter(is_connected=True).count()
    if computers_connected != 0:
        connected_precentage = int(computers_online / computers_connected * 100)
    else:
        connected_precentage = -1
    return render(request, 'index.html',
                  {
                      'computers_connected': computers_connected,
                      'connected_precentage': connected_precentage,
                      'bar_status': bar_status
                  })

def computers(request):
    clients = Client.objects.all()
    bar_status = False
    if 'sidebar' in request.COOKIES.keys():
        bar_status = request.COOKIES['sidebar']
    print(bar_status)
    return render(request, 'computers.html',
                  {
                      'clients': clients,
                      'bar_status': bar_status
                  })
