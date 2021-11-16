from django.db import models
from accounts.models import CustomUser
from maqola.models import Article


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.user}-{self.article}"