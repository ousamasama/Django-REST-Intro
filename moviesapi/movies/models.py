from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True, related_name='movies')

    def __str__(self):
        return self.title

    class Meta:
        #tuple so it needs comma
        ordering = ('title',)

class Director(models.Model):
    name = models.CharField(max_length=50)
    is_arrogant_jerk = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(blank=False)
    movie_cast_in = models.ForeignKey('Movie', on_delete=models.SET_NULL, null=True, related_name='actors')

    def __str__(self):
        return self.first_name + self.last_name