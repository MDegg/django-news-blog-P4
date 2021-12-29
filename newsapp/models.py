from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from cloudinary.models import CloudinaryField
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default = "Django News")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #feature_image = CloudinaryField('image', default='placeholder')
    #created_on = models.DateField(auto_now_add = True)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    
    #created_on = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

    
