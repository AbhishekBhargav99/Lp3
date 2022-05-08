from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import *
from .models import *

# Create your views here.
def showtasks(request):
    t = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': t})

def addtask(request):
    t = Task()
    t.name = request.GET.get('taskname')
    t.save()
    return redirect('showtasks')

@csrf_exempt
def deleteone(request):
    t = Task.objects.get(name = request.POST.get('taskname'))
    t.delete()
    return redirect('showtasks')

@csrf_exempt
def complete(request):
    t = Task.objects.get(name = request.POST.get('taskname'))
    t.complete = True
    t.save()
    return redirect('showtasks')

@csrf_exempt
def deletealltasks(request):
    if request.user.is_superuser:
        t = Task.objects.all()
        for tsk in t:
            tsk.delete()
        return redirect('showtasks')
    else:
        return HttpResponse("<h2>Returned status: Error 403: forbidden<br>Permission Denied</h2>")
