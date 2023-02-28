from django.shortcuts import render

# Create your views here.

def landing_page(request):
    context = {
        'is_landing_page': True,
    }
    return render(request, 'home/partials/index.html', context,)    

def home(request):
    ...

def login(request):
    ...