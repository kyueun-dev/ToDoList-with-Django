from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
"""HttpResponse는 인자로 받은 문자열을 사용자의 화면에 보여주도록 하는 함수"""
from .models import *
from django.urls import reverse

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    content = {'todos': todos}
    return render(request, 'my_to_do_app/index.html', content)

def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))
    #return HttpResponse("create Todo를 할 거야! =>" + user_input_str)