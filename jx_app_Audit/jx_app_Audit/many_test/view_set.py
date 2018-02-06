from models import Author,Book
from rest_framework import viewsets
from serializer import AuthorSerializer, BookSerializer

from django_filters.rest_framework import DjangoFilterBackend

class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Author.objects.all().order_by('-first_name')
    serializer_class = AuthorSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('first_name','last_name',)
    search_fields = ('first_name','last_name$',)
    ordering_fields = ('first_name',)
    
   


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('title',)
    ordering_fields = ('first_name',)
    
    
 