from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from COMSAPI.models import Client, Module, Task, Report, TASK_STATUS


def bar_status(request):
    bar = False
    if 'sidebar' in request.COOKIES.keys():
        bar = request.COOKIES['sidebar']
    return bar


# Create your views here.
def index(request):        
    computers_connected = Client.objects.count()
    computers_online = Client.objects.filter(is_connected=True).count()
    
    if computers_connected != 0:
        connected_precentage = int(computers_online / computers_connected * 100)
    else:
        connected_precentage = -1

    tasks_pending = Task.objects.filter(status=TASK_STATUS.PENDING).count()
    tasks_finished = Task.objects.filter(status=TASK_STATUS.FINISHED).count()
    
    return render(request, 'index.html',
                  {
                      'computers_connected': computers_connected,
                      'computers_online': computers_online,
                      'computers_offline': computers_connected - computers_online,
                      'connected_precentage': connected_precentage,
                      'tasks_pending': tasks_pending,
                      'tasks_finished': tasks_finished,
                      'page_title': 'index',
                      'bar_status': bar_status(request)
                  })

def computers(request):
    clients = Client.objects.all()
    return render(request, 'computers.html',
                  {
                      'clients': clients,
                      'page_title': 'computers',
                      'bar_status': bar_status(request)
                  })

def modules(request):
    modules = Module.objects.all()
    return render(request, 'modules.html',
                    {
                        'modules': modules,
                        'page_title': 'modules',
                        'bar_status': bar_status(request)
                    })

def tasks(request):
    tasks = Task.objects.all()
    modules = Module.objects.all()
    clients = Client.objects.all()
    return render(request, 'tasks.html',
                      {
                          'tasks': tasks,
                          'clients': clients,
                          'modules': modules,
                          'modules_count': len(modules),
                          'page_title': 'tasks',
                          'bar_status': bar_status(request)
                      })

def view_task(request, id):
    task = Task.objects.get(id=id)
    reports = Report.objects.filter(task=task).all()
    return render(request, 'task.html',
                      {
                          'task': task,
                          'reports': reports
                          })

@csrf_exempt
def new_module(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'wrong request'})
    
    if 'file' not in request.FILES.keys():
        return JsonResponse({'error': 'no file'})
    file_ = request.FILES['file']
    
    if 'name' not in request.POST.keys() or request.POST['name'] == '':
        return JsonResponse({'error': 'no name'})
    name = request.POST['name']

    new_module = Module(name=name, file=file_)
    new_module.save()
    
    return JsonResponse({'result': 'ok', 'id': new_module.id})


@csrf_exempt
def new_task(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'wrong request'})

    if 'name' not in request.POST.keys():
        return JsonResponse({'error': 'no name'})
    name = request.POST['name']
    
    if 'args' not in request.POST.keys():
        return JsonResponse({'error': 'no args'})
    args = request.POST['args']
    
    if 'module' not in request.POST.keys():
        return JsonResponse({'error': 'no module'})
    module = Module.objects.get(id=int(request.POST['module']))
    
    if 'clients' not in request.POST.keys():
        return JsonResponse({'error': 'no clients'})
    clients = request.POST['clients'].split(',')

    task_ids = []

    for client_id in clients:
        client = Client.objects.get(id=client_id)
        new_task = Task(name=name, arguments=args, module=module, client=client, status=TASK_STATUS.PENDING)
        new_task.save()
        task_ids.append(new_task.id)
    
    return JsonResponse({'result': 'ok', 'id': task_ids})


@csrf_exempt
def new_task(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'wrong request'})

    if 'name' not in request.POST.keys():
        return JsonResponse({'error': 'no name'})
    name = request.POST['name']
    
    if 'args' not in request.POST.keys():
        return JsonResponse({'error': 'no args'})
    args = request.POST['args']
    
    if 'module' not in request.POST.keys():
        return JsonResponse({'error': 'no module'})
    module = Module.objects.get(id=int(request.POST['module']))
    
    if 'clients' not in request.POST.keys():
        return JsonResponse({'error': 'no clients'})
    clients = request.POST['clients'].split(',')

    task_ids = []

    for client_id in clients:
        client = Client.objects.get(id=client_id)
        new_task = Task(name=name, arguments=args, module=module, client=client, status=TASK_STATUS.PENDING)
        new_task.save()
        task_ids.append(new_task.id)
    
    return JsonResponse({'result': 'ok', 'id': task_ids})

@csrf_exempt
def delete_computer(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'wrong request'})

    if 'id' not in request.POST.keys():
        return JsonResponse({'error': 'no id'})

    computer = Client.objects.get(id=request.POST['id'])
    computer.delete()
    return JsonResponse({'result': 'ok'})

@csrf_exempt
def delete_task(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'wrong request'})

    if 'id' not in request.POST.keys():
        return JsonResponse({'error': 'no id'})

    task = Task.objects.get(id=request.POST['id'])
    task.delete()
    return JsonResponse({'result': 'ok'})
