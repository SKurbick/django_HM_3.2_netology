from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = [book for book in Book.objects.all()]
    context = {'books': books,
               }
    return render(request, template, context)


def pub_date(request, pub_date):
    content = sorted([str(b.pub_date) for b in Book.objects.all()])
    previous_page = content[content.index(pub_date) - 1]

    if content[-1] == previous_page:
        previous_page = False

    if content[-1] == pub_date:
        next_page = False
    else:
        next_page = content[content.index(pub_date) + 1]

    books = Book.objects.filter(pub_date=pub_date)
    context = {'books': books,
               'next_page': next_page,
               'previous_page': previous_page,
               }
    template = 'books/pub_date.html'
    return render(request, template, context)
