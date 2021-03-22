from django.contrib import admin
from .models import SongModel, InterpreterModel, LinksSongsModel

# Register your models here.

admin.site.register(SongModel)
admin.site.register(InterpreterModel)
admin.site.register(LinksSongsModel)