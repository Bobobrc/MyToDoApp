from django.shortcuts import render, redirect, get_object_or_404
from todoapp.models import List, Task

# Create your views here.
def MainPage(request):
  if request.method=='POST':
    if request.POST['Submit'] == 'create_list':
      list_name = request.POST['list_name']
      password = request.POST['password']
      list = List(name=list_name, password = password)
      list.save()
      return redirect('list', list_name=list_name)
    else:
      list_name = request.POST['list_name']
      return redirect('list', list_name=list_name)
  return render(request, 'firstpage.html')

def Lists(request, list_name):
  list = get_object_or_404(List, name=list_name)
  if request.method=="POST":
    if request.POST['Submit']=='add_task':
      task_name = request.POST['task_name']
      password = request.POST['password']
      important = request.POST.get('important', False)
      if password == list.password:
        task = Task(list=list, task_name=task_name, important=important, done=False)
        task.save()
    else:
      password = request.POST['password']
      done = request.POST.getlist('done')
      important = request.POST.getlist('important')
      normal = request.POST.getlist('normal')
      delete = request.POST.getlist('delete')
      if password == list.password:
        for task in delete:
          dels = Task.objects.get(list=list, task_name = task)
          dels.delete()
        for task in normal:
          nm = Task.objects.get(list=list, task_name = task)
          nm.important = False
          nm.done = False
          nm.save()
        for task in important:
          imp = Task.objects.get(list=list, task_name = task)
          imp.important = True
          imp.done = False
          imp.save()
        for task in done:
          dn = Task.objects.get(list=list, task_name = task)
          dn.done = True
          dn.save()
    return redirect('list', list_name=list.name)
  tasks = Task.objects.filter(list__name = list_name, important = False, done = False)
  important_tasks = Task.objects.filter(list__name=list_name, important = True, done=False)
  done_tasks = Task.objects.filter(list__name = list_name, done=True)
  return render(request, 'list.html', {'list':list, 'tasks':tasks, 'important_tasks':important_tasks, 'done_tasks':done_tasks})