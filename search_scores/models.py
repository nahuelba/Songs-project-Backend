from django.db import models
from django.conf import settings
from songoftheday.models import SongModel, InterpreterModel

# Create your models here.


class EditorialModel(models.Model):
    Editorial= models.CharField(max_length=200)

    def __str__(self):
        return self.Editorial


class ScoresModel(models.Model):
    song = models.ForeignKey(SongModel , on_delete=models.CASCADE, null=True)
    editorial= models.ForeignKey(EditorialModel, on_delete=models.CASCADE, null=True)
    score = models.FileField(upload_to="scores/%Y/%m/%d/")
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.song)

    class Meta:
        verbose_name= "Score"
        verbose_name_plural="Scores"


