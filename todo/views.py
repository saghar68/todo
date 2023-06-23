from django.shortcuts import render,redirect
from .models import TODO
# Create your views here.

def test(request):
    notes=TODO.objects.all()
    return render(request,'todo/home.html',{'notes':notes})


def delete(request,todo_id):
    notes=TODO.objects.get(id=todo_id)
    notes.delete()
    return redirect('todo')
  