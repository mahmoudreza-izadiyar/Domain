from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('bands', views.BandsViewSet)
router.register('albums', views.AlbumsViewSet)
router.register('artists', views.ArtistsViewSet)
router.register('songs', views.SongsViewSet)
router.register('copy-rights', views.CopysRightsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]