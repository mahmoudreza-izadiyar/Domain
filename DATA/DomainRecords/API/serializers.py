from rest_framework import serializers
from .models import Bands, Albums, Artists, Songs, CopyRights

class BandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bands
        fields = ['name']

class ArtistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        fields = ['first_name', 'last_name', 'band_id', 'date_of_joined', 'date_of_left']

class AlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albums
        fields = ['artist_id', 'title', 'release_date', 'band_id']


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ['name', 'band_id', 'release_date', 'artist_id', 'album_id']

class CopysRightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CopyRights
        fields = ['album_id', 'band_id', 'release_date', 'song_id']
