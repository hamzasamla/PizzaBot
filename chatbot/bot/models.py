from django.db import models

class Message(models.Model):
    message=models.CharField(max_length=500)
    sender=models.CharField(max_length=500)
    created=models.DateTimeField(auto_now=True)

def __str__(self):
    return self.sender+': '+self.message