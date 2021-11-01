from django.db import models


class Bands(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Artists(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    band_id = models.ForeignKey(Bands, on_delete=models.DO_NOTHING)
    date_of_joined = models.DateField(max_length=100)
    date_of_left = models.DateField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.first_name



class Albums(models.Model):
    artist_id = models.ForeignKey(Artists, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    band_id = models.ForeignKey(Bands, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Songs(models.Model):
    name = models.CharField(max_length=100)
    band_id = models.IntegerField()
    release_date = models.DateField()
    artist_id = models.ForeignKey(Artists, on_delete=models.PROTECT)
    album_id = models.ForeignKey(Albums, on_delete=models.PROTECT)
    def __str__(self):
        return self.name

class CopyRights(models.Model):
    album_id = models.ForeignKey(Albums, on_delete=models.PROTECT)
    band_id = models.IntegerField()
    song_id = models.ForeignKey(Songs, on_delete=models.PROTECT)
    release_date = models.DateField()
    is_valid = models.BooleanField(blank=True, null=True)
    def __int__(self):
        return self.album_id