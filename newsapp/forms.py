from django import forms
from .models import Post, Category, Comment


choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author',
                  'category', 'body', 'feature_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder':
                                            'Add Blog Title Here.....'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder':
                                                'Add Blog Title Tag Here.....'}),
            'author': forms.TextInput(attrs={'class': 'form-control',
                                             'value': '', 'id': 'user',
                                             'type': 'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Add Blog Body Here.....'}),


        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Add Blog Title Here.....'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Add Blog TitleTag Here.....'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Add Blog Body Here.....'}),

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }
