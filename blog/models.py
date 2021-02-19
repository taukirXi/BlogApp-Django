from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    pub_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title + ' | '+ str(self.author)

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name + ' | ' + self.email