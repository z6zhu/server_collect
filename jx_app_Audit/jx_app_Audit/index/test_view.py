# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.http import HttpResponseRedirect  
from django.http.response import HttpResponse  
from django.core.urlresolvers import reverse
import json,re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from model_foreign import Membership,Person
from model_many import IndexBook,IndexAuthor,IndexBookAuthor
import datetime


# the function is for foreighkey
def test_test(request):

    gg=Person.objects.create(name="zhu113")
    Membership.objects.create(person=gg,invite_reason='mmmmmmmm')
 # database is restrict(default) you must update it to cascade
    Person.objects.filter(name="zhu113").update(name="ggg")

    return render(request, "TEST_TEST.html")

def many_many(request):
     
    bo=IndexBook.objects.create(title="i")
    au=IndexAuthor.objects.create(first_name="vv",last_name="v")
    ss=IndexBookAuthor(book=bo,author=au)
    ss.save()  
    print "------------",ss.book.title
    print "------------",ss.author.first_name
    return render(request, "Many_Many.html")

def vue_test(request):
    
     return render(request, "vue_test.html")
    