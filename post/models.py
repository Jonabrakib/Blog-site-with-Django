from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):

        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    Featured = models.BooleanField(default=False)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_view', kwargs={
            'id':self.id
        })


class Subscriber(models.Model):
    email=models.EmailField()
    timestamp =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email