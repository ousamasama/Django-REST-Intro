from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from movies.models import Movie, Director, Actor
from movies.serializers import MovieSerializer, DirectorSerializer, ActorSerializer
# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'movies': reverse('movies', request=request, format=format),
        'directors': reverse('directors', request=request, format=format),
        'actors': reverse('actors', request=request, format=format)
    })

class MovieViewSet(viewsets.ModelViewSet):
    #what is the queryset/what to go get
    queryset = Movie.objects.all()
    #what serializer to use to do translations
    serializer_class = MovieSerializer

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer