from django.db import models
from django.contrib.auth.models import User

class MyUser(models.Model):
    user = models.OneToOneField(User)

class Neighbour(models.Model):
    user = models.ForeignKey(User,related_name='user',null=True)
    name = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name 

class Message(models.Model):
    sender = models.ForeignKey(User,related_name='sender')
    recipient = models.ManyToManyField(Neighbour)
    content = models.TextField(max_length=100)

    def __str__(self):
        return self.content[:20] + ' ...'