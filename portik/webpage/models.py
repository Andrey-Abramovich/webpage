from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)
    subscribers = models.ManyToManyField(User)

    def __str__(self):
        return self


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    content = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    foto = models.ImageField(width_field=256, height_field=256)
    postcategory = models.ManyToManyField(Category)


    def __str__(self):
        return self



    def like(self):
        self.rating += 1
        self.save()

    def dizlike(self):
        self.rating -= 1
        self.save()


