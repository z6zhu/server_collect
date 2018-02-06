# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from models import Author,Book

def many_2_many(request):
    
#     b=Book.objects.create(title="maxi")
#     a=Author.objects.create(first_name="nn",last_name="dd",email="qq@qq.com")
#     b.authors.add(a)
       
         
    # the function of remove is jiut to delete the relationship between  """Book"""   and  """Author"""    
    # you want to delete the book aor author  data =====you must to use model the function of delete
           
#     b=Book.objects.get(title="django")
#     a=Author.objects.get(first_name="vv")
#     b.authors.remove(a)
#     Book.objects.get(title="django").delete()
#     Author.objects.get(first_name="vv").delete()
#         
#     qu_set=b.authors.all()
#     for i in qu_set:
#         print i.email
#          
#     go_set=a.book_set.all()
#     for i in go_set:
#         print i.title

    
        
    return render(request,"TEST_TEST2.html")