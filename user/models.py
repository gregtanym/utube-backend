from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    # subscriptions = user_set or foriegn key to many user profiles
    # saved = video_set or foreign key to many video models 