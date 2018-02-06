from models import Author,Book
from rest_framework import serializers


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'email')


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'authors')
        
