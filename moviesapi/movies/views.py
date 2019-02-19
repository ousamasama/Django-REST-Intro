from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import filters
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

    #tuple
    filter_backends = (filters.SearchFilter,)
    #what the search is applying to
    search_fields = ('title','year')

    # def get_queryset(self):
    #     query_set = Movie.objects.all()
    #     #query params comes back as dicionary
    #     keyword = self.request.query_params.get('search', None)
    #     if keyword is not None:
    #         print("query params", keyword)
    #         # dunderscore icontains
    #         query_set = query_set.filter(title__icontains=keyword)
    #     return query_set

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    def get_queryset(self):
        queryset = Director.objects.all()
        keyword = self.request.query_params.get('jerk', None)
        if keyword is not None:
            queryset = queryset.filter(is_arrogant_jerk=True)
        return queryset

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer