from django.test import TestCase
from django.db import models



# Create your tests here.

class TestModel(TestCase):
    """testing profile model"""
    def test_profile_model(self):

        user = models.OneToOneField(User, null=True, on_delete= models.CASCADE)
        bio = RichTextField(blank = True, null=True)
        profile_pic = CloudinaryField('image', default='placeholder')
        facebook_url = models.CharField(max_length=255, blank = True, null=True)
        twitter_url = models.CharField(max_length=255, blank = True, null=True)
        instagram_url = models.CharField(max_length=255, blank = True, null=True)


        """ test str is returned """
        def __str__(self):
            return str(self.user) 