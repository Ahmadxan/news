import datetime
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


class Category(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='category_author')
    editor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='category_editor', null=True)
    title = models.CharField(max_length=100)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title