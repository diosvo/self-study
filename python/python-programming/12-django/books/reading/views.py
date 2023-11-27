from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Book


def index(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    return render(request, 'reading/index.html', {'books': books})


def info(request: HttpRequest, book_id: int) -> HttpResponse:
    book = Book.objects.get(pk=book_id)
    return render(request, 'reading/info.html', {'book': book})
