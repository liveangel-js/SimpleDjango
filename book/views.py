# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from book.models import *
from django.core.cache import cache

def booklist(request):
    if cache.get('book'):
        books = cache.get('book')
    else:
        books = Book.objects.all()
        cache.set('book', books)

    if cache.get('publishers'):
        publishers = cache.get('publisher')
    else:
        publishers = Publisher.objects.all()
        cache.set('publishers', publishers)

    if cache.get('authors'):
        authors = cache.get('authors')
    else:
        authors = Author.objects.all()
        cache.set('authors', authors)



    #software engineer 的数量
    b_count = Book.objects.get_book_count('software engineer')


    t = loader.get_template("booklist.html")
    c = Context({'books': books, 'publishers':publishers, 'authors':authors, 'bcount': b_count})

    return HttpResponse(t.render(c))