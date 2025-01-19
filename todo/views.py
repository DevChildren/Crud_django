from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Todo
from django.views.decorators.http import require_POST, require_GET

def index(request):
  items = Todo.objects.order_by('-id')
  return render(request, 'todo/index.html', {'items': items})
def done(request):
  items = Todo.objects.filter(status=True).order_by('-id')
  return render(request, 'todo/index.html', {'items': items})
def pending(request):
  items = Todo.objects.filter(status=False).order_by('-id')
  return render(request, 'todo/index.html', {'items': items})

@require_GET
def delete_all(request):
  todo = Todo.objects.all()
  todo.delete()
  return HttpResponseRedirect(reverse('index'))

@require_GET
def delete(request, id):
  try:
    Todo.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('index'))
  except ObjectDoesNotExist:
    return HttpResponse('Gagal bro')

@require_POST    
def create(request):
  todo = request.POST['title']
  if len(todo) <= 0:
      return HttpResponse('text kosong')
  try:
    todo = request.POST['title']
    # Cek apakah judul sudah ada di database
    if Todo.objects.filter(title=todo).exists():
        return HttpResponse("Judul sudah ada!", status=400)
    # Simpan data baru
    Todo.objects.create(title=todo)
    items = Todo.objects.order_by('-id')
    return HttpResponseRedirect(reverse('index'))
  except exceptions:
    return HttpResponse('Gagal bro')
    
@require_POST
def update(request, id):
  print(id)
  try:
    todo = Todo.objects.get(id=id)
    todo.status = not todo.status
    todo.save()
    
    return HttpResponseRedirect(reverse('index'))
  except ObjectDoesNotExist:
    return HttpResponseRedirect(reverse('index'))

