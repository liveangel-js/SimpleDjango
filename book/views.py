# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from book.models import *

def booklist(request):
    books = Book.objects.all()
    publishers = Publisher.objects.all()
    authors = Author.objects.all()
    #software engineer 的数量
    b_count = Book.objects.get_book_count('software engineer')


    t = loader.get_template("booklist.html")
    c = Context({'books': books, 'publishers':publishers, 'authors':authors, 'bcount': b_count})

    return HttpResponse(t.render(c))