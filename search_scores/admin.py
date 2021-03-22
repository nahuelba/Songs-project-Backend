from django.contrib import admin
from .models import ScoresModel,EditorialModel

# Register your models here.
class ScoresAdmin(admin.ModelAdmin):
    readonly_fields=['created',]

admin.site.register(ScoresModel, ScoresAdmin)
admin.site.register(EditorialModel)
