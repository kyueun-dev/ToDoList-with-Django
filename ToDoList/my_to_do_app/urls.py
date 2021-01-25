# TodoList > my_to_do_app > urls.py
from django.urls import path
from . import views  # 같은 경로는 . 로 표시

urlpatterns = [
    path('', views.index, name='index'),  # 쉼표를 까먹지 말자
    path('createTodo/', views.createTodo, name='createTodo'),
    path('deleteTodo/', views.doneTodo, name='deleteTodo')
]