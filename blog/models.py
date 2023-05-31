from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True)
    description = models.TextField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title

