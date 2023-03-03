from django.shortcuts import render

# Create your views here.

def settings(request):
    context = {

    }
    return render(request, 'settings/pages/settings.html')