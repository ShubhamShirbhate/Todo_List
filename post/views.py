from django.shortcuts import render, get_object_or_404, redirect
from account.models import Todoo
from account.forms import Todooform
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'post/home.html')

@login_required
def currenttodo(request):
    todo = Todoo.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'post/currenttodo.html', {'todo':todo})

@login_required
def completetodos(request):
    todo = Todoo.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'post/completetodos.html', {'todo':todo})

@login_required
def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todoo, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = Todooform(instance=todo)
        return render(request, 'post/viewtodo.html', {'todo':todo, 'form':form})
    else: 
        try:
            form = Todooform(request.POST, instance=todo)
            form.save()
            return redirect('currenttodo')
        except ValueError:
            return render(request, 'post/viewtodo.html', {'todo':todo, 'form':form, 'error':'bad info'})
            
@login_required
def completetodo(request, todo_pk):
    todo = get_object_or_404(Todoo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('currenttodo')
        
@login_required
def deletetodo(request, todo_pk):
    todo = get_object_or_404(Todoo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.delete()
        return redirect('currenttodo')
