from django.contrib import admin
from .models import Songs, Albums, Artists, CopyRights, Bands

admin.site.register(Songs)
admin.site.register(Albums)
admin.site.register(Artists)
admin.site.register(CopyRights)
admin.site.register(Bands)