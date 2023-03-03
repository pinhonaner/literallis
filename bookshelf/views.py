from django.shortcuts import render

# Create your views here.

def bookshelf(request):
    context = {
        'user_id': ...,
        'category': ...,
        'genre': ...,
        'title': 'Prateleira | Literallis',
    }
    return render(request, 'bookshelf/pages/bookshelf.html')

def book(request):
    context = {
        'book_id': ...,
        'title': f'{"book"} | Literallis',
    }
    return render(request, 'booksehlf/pages/book.html' )
