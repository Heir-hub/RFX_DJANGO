from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
        title = models.CharField(max_length = 150)
        content = models.TextField()
        Image = models.ImageField(upload_to = 'picture', max_length = 300, blank=True, null =True)
        date = models.DateTimeField(default = timezone.now)
        author = models.ForeignKey(User, on_delete=models.CASCADE)

        def __str__(self):
            return self.title
        
    
        def get_absolute_url(self):
            return reverse('blog-detail',kwargs = {'pk': self.pk})

   