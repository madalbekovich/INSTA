from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Login

def view(request):
    if request.method == 'POST':
        # Получаем данные из POST-запроса
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Сохраняем данные в базу данных
        user_profile = Login(username=username, password=password)
        user_profile.save()

        # Возвращаем HTTP-ответ, например, сообщение об успешной обработке
        return render(request, 'index.html')
    else:
        # Если это не POST-запрос, просто отобразим шаблон с формой
        return render(request, 'index.html')

def success_page(request):
    return render(request, 'index.html')