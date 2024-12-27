from django.shortcuts import render, redirect
from .models import UserInput
from .forms import UserInputForm

def news_home(request):
    return render(request, 'news/news_home.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'news/create.html')
        else:
            error = 'Введён неккоректный ответ'


    else:
        form = UserInputForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)
# Create your views here.
