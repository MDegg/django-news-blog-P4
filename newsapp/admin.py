from django.contrib import admin
from .models import Post, Category
#from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Post)
admin.site.register(Category)