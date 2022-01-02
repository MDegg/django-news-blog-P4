from django.contrib import admin
from .models import Post, Category, Profile
#from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)