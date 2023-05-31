from django.db import models
from django.contrib.auth.models import User


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
class Contact(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    message = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

