from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class user_profile(models.Model):

    #using default User model by linking 
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional fields
    email = models.EmailField(blank = True)
    website = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures' , blank = True )
    bio = models.CharField(blank=True, max_length=300)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('homepage:profile')
