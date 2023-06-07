from django.shortcuts import render,redirect
from home.models import Task

def home(request):
    context={'success': False, 'name': 'Anurag'}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context={'success':True}
    return render (request,'home.html',context)

def task(request):
    allTasks=Task.objects.all()
    context={'tasks':allTasks}
    return render (request,'task.html',context)

def edit(request, title):
    current=Task.objects.get(taskTitle=title)
    if request.method == "POST":
        current.taskTitle=request.POST['title']
        current.taskDesc=request.POST['desc']

    current.save()
    context={'object':current}
    return render (request,'edit.html',context)

def delete(request, title):
    try:
        current1=Task.objects.get(id=title)
        current1.delete()
        return redirect(request,'task.html')
    except:
        return redirect ('/task')




