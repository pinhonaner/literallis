from django.shortcuts import render

# Create your views here.

def landing_page(request):
    context = {
        'is_landing_page': True,
        'title': 'Bem vindo | Literallis',
    }
    return render(request, 'home/pages/index.html', context,)    

def home(request):
    context = {
        'is_landing_page': False,
        'title': 'Literallis',
    }
    return render(request, 'home/pages/home.html', context)
    ...

def login(request):
    context = {
        'is_landing_page': False,
        'title': 'Login | Literallis',
    }
    return render(request, 'home/pages/login.html', context)
    ...

def about(request):
    context = {
        'is_landing_page': False,
        'title': 'Sobre | Literallis',
    }
    return render(request, 'home/pages/about.html', context)
    ...

def contact(request):
    context = {
        'is_landing_page': False,
        'title': 'Contato | Literallis',
    }
    return render(request, 'home/pages/contact.html', context)
    ...