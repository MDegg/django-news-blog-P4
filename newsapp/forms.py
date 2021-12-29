from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add Blog Title Here.....'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder':'Add Blog Title Tag Here.....'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Add Blog Body Here.....'}),

        }