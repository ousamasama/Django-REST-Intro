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
    # path('', include(router.urls))
    #how to if it had versions
    path('api/v1/', include(router.urls))
    # path('api/v2', include(router.urls))
]