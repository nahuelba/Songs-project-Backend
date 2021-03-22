from django.db import models

# Create your models here.

class InterpreterModel(models.Model):
    interpreter_name=models.CharField(max_length=100)
    interpreter_image=models.ImageField(upload_to="artistimages")
    
    
    def __str__(self):
        return self.interpreter_name

    class Meta:
        verbose_name= "Interpreter"
        verbose_name_plural="Interpreters"

class LinksSongsModel(models.Model):
    song_title=models.CharField(max_length=100, null=True)
    interpreters=models.ManyToManyField(InterpreterModel)
    embed_youtube_link=models.URLField(max_length=200, null=True, blank=True)
    embed_spotify_link=models.URLField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        interpreters = ", ".join(str(seg) for seg in self.interpreters.all())
        return '{}, {}'.format(self.song_title, interpreters)
    
    class Meta:
        verbose_name= "Link"
        verbose_name_plural="Links"
    

class SongModel(models.Model):
    song_title=models.CharField(max_length=100)
    composer=models.ForeignKey(InterpreterModel, on_delete=models.CASCADE, null=True)
    links= models.ManyToManyField(LinksSongsModel)
    date_song=models.CharField(max_length=5, unique=True)
    
    

    def __str__(self):
        return self.song_title

    class Meta:
        verbose_name= "Song"
        verbose_name_plural="Songs"

