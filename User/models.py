from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    '''
        Post Model stores the Post Details\n
        Having one Foreign key from User Model.
    '''
    user = models.ForeignKey(User, verbose_name="User Object", on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Post Text')
    created_at = models.DateTimeField(verbose_name="Post Created at", auto_now_add=True,)
    updated_at = models.DateTimeField(verbose_name='Last Updated at', auto_now=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'{self.user.username} - {self.text[0:20]}'

    @staticmethod
    def autocomplete_search_fields():
        return 'user__username'
