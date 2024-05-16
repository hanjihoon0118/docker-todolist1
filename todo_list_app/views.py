# todo_list_app/views.py

from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')  # ���� ��� �������� �����̷�Ʈ
    else:
        form = TodoForm()
    return render(request, 'add_todo.html', {'form': form})
