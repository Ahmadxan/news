import datetime
from django.db import models
from django.contrib.auth import get_user_model
from category.models import Category


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='article_author')
    editor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='article_editor', null=True)
    title = models.CharField(max_length=200, blank=False, null=False)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title
