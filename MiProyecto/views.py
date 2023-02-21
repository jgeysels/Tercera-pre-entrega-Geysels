from django.shortcuts import render
from .models import Author, Book, Publisher

# Create your views here.

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publishers': publishers})
