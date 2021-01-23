# my_to_do_app > urls.py
from django.urls import path
from . import views  # 같은 경로는 . 로 표시

urlpatterns = [
    path('', views.index, name='index'),
    path('createTodo/', views.createTodo, name='createTodo')
]