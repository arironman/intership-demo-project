from django import forms
from django.db.models import fields
from User.models import Post
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    '''
        Form for Post model
    '''

    class Meta:
        model = Post
        fields = ['text']


    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        # adding attributes(class, id etc) to the form field
        self.fields['text'].widget.attrs['class'] = 'post-form-field'
        self.fields['text'].widget.attrs['placeholder'] = 'Enter Your Post Here....'

