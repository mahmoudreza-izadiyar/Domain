from django.shortcuts import render


from django.urls import path, include
from .models import Bands, Albums, Artists, Songs, CopyRights
from .serializers import BandsSerializer, ArtistsSerializer, AlbumsSerializer, SongsSerializer, CopysRightsSerializer
from rest_framework import viewsets


class BandsViewSet(viewsets.ModelViewSet):
    queryset = Bands.objects.all()
    serializer_class = BandsSerializer

class ArtistsViewSet(viewsets.ModelViewSet):
    queryset = Artists.objects.all()
    serializer_class = ArtistsSerializer

class AlbumsViewSet(viewsets.ModelViewSet):
    queryset = Albums.objects.all()
    serializer_class = AlbumsSerializer

class SongsViewSet(viewsets.ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer

class CopysRightsViewSet(viewsets.ModelViewSet):
    queryset = CopyRights.objects.all()
    serializer_class = CopysRightsSerializer