from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from movies import views

router = DefaultRouter()
#first movies for route, second movies for naming convention('movies, views.MovieViewSet, 'movies')
router.register('movies', views.MovieViewSet)
router.register('directors', views.DirectorViewSet)
router.register('actors', views.ActorViewSet)


urlpatterns = [
    path('', include(router.urls))
]