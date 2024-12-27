from django.shortcuts import render, redirect
from .models import UserInput
from .forms import UserInputForm





def page(request):
    return render(request, "main/page.html")

def page0(request):
    return render(request, "main/page0.html")

def page1(request):
    return render(request, "main/page1.html")

def page2(request):
    return render(request, "main/page2.html")

def page3(request):
    return render(request, "main/page3.html")

def page4(request):
    return render(request, "main/page4.html")

def page5(request):
    return render(request, "main/page5.html")

def page6(request):
    return render(request, "main/page6.html")

def page7(request):
    return render(request, "main/page7.html")

def page8(request):
    return render(request, "main/page8.html")

def page9(request):
    return render(request, "main/page9.html")

def page10(request):
    return render(request, "main/page10.html")

def page11(request):
    return render(request, "main/page11.html")

def page12(request):
    return render(request, "main/page12.html")

def page13(request):
    return render(request, "main/page13.html")

def politicconf(request):
    return render(request, "main/politicconf.html")

def rules(request):
    return render(request, "main/rules.html")

def faq(request):
    return render(request, "main/faq.html")

def aboutus(request):
    return render(request, "main/aboutus.html")


def page1(request):
    error = ''
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/page1.html')
        else:
            error = 'Введён неккоректный ответ'


    else:
        form = UserInputForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/page1.html', data)

def page0(request):
    error = ''
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/page0.html')
        else:
            error = 'Введён неккоректный ответ'


    else:
        form = UserInputForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/page0.html', data)

def page3(request):
    error = ''
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/page3.html')
        else:
            error = 'Введён неккоректный ответ'


    else:
        form = UserInputForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/page3.html', data)

def page4(request):
    error = ''
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/page4.html')
        else:
            error = 'Введён неккоректный ответ'


    else:
        form = UserInputForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/page4.html', data)

def page2(request):
    error = ''
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/page2.html')
        else:
            error = 'Введён неккоректный ответ'


    else:
        form = UserInputForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/page2.html', data)

def page5(request):
    error = ''
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/page5.html')
        else:
            error = 'Введён неккоректный ответ'


    else:
        form = UserInputForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/page5.html', data)


def page6(request):
    error = ''
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/page6.html')
        else:
            error = 'Введён неккоректный ответ'


    else:
        form = UserInputForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/page6.html', data)

def page8(request):
    error = ''
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/page8.html')
        else:
            error = 'Введён неккоректный ответ'


    else:
        form = UserInputForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/page8.html', data)

def page9(request):
    error = ''
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/page9.html')
        else:
            error = 'Введён неккоректный ответ'


    else:
        form = UserInputForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/page9.html', data)

def page10(request):
    error = ''
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/page10.html')
        else:
            error = 'Введён неккоректный ответ'


    else:
        form = UserInputForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/page10.html', data)

def page11(request):
    error = ''
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/page11.html')
        else:
            error = 'Введён неккоректный ответ'


    else:
        form = UserInputForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/page11.html', data)

def page14(request):
    error = ''
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/page14.html')
        else:
            error = 'Введён неккоректный ответ'


    else:
        form = UserInputForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/page14.html', data)



