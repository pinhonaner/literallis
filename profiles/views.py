from django.shortcuts import render

# Create your views here.

def profile_page(request):
    context = {
        'profile_id': ...,
        'title': f'{"profile_id"} | Literallis',
    }
    return render(request, 'profiles/pages/profile.html', context)
