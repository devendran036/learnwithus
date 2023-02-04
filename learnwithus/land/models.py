from django.db import models
class userinfo(models.Model):
    username=models.CharField(max_length=200)
    passw=models.CharField(max_length=200)
    def __str__(self):
        return self.username

# Create your models here.
