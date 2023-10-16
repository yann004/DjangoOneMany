from django.shortcuts import render
from library.models import Author, Book

def display_data(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    return render(request, 'library/page.html', {'authors': authors, 'books': books})
 
   # Nouvelles vues pour les détails de l'auteur et du livre

def author_detail(request, author_id):
    author = Author.objects.get(pk=author_id)
    return render(request, 'library/author_detail.html', {'author': author})

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'library/book_detail.html', {'book': book})
 
   