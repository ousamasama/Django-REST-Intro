from rest_framework import serializers
#pythonic way to not have more imports than necessary
from movies.models import Movie, Director, Actor

class DirectorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Director
        # can somehow do fields = __all__ ?
        # fields = "__all__"
        fields = ('name', 'is_arrogant_jerk', 'movies')


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    # if you access a serializer inside another, you can get a subquery that shows the extra information
    # encouraged to not do this because it keeps it flat
    # without read only you can update DirectorSerializer()
    # can also add read_only_fields until meta
    # director = DirectorSerializer(read_only=True)

    class Meta:
        model = Movie
        fields = ('title', 'year', 'director', 'actor')

class ActorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Actor
        fields = ('first_name', 'last_name', 'age', 'movies')