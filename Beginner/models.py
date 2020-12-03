
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class BeginnerTutorial(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    videos = models.FileField(upload_to = 'Video', max_length = 300, blank=True, null =True)
    date = models.DateTimeField(default = timezone.now)
    author =  models.ForeignKey(User, on_delete=models.CASCADE,related_name='beginner_author')
  
   

    def __str__(self):
        return self.title

   




