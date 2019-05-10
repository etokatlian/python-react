from django.db import models
import uuid


class Author(models.Model):

    """Summary

    Attributes:
        first_name (string): author first name
        last_name (string): author last name
        username (string): author username
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Post(models.Model):

    """Summary

    Attributes:
        author (string): author username
        content (string): content of the post
        created_at (string): post creation date
        title (string): title of the post
    """

    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=10000)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} ({self.title})'
