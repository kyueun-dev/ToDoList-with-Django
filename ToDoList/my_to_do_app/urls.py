# TodoList > my_to_do_app > urls.py
from django.urls import path
from . import views  # 같은 경로는 . 로 표시  # 파일을 임포트한 거구나

urlpatterns = [
    path('', views.index, name='index'),  # 쉼표를 까먹지 말자
    path('createTodo/', views.createTodo, name='createTodo'),
    path('doneTodo/', views.doneTodo, name='doneTodo')  # views파일에서 doneTodo로 처리하란 뜻
]