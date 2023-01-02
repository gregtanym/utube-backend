from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from user.models import User

# Create your models here.
CATEGORIES = (
    ('GM','Gaming'),
    ('MV','Movies'), 
    ('ED','Education'), 
    ('MC','Music'),
    ('TE','Technology'),
    ('NW','News'), 
    ('SP','Sports'),
    ('FB','Fashion & Beauty'),
)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, blank=True, null=True)   
    text = models.CharField(max_length=9999)
    image = models.ImageField(max_length=100)

class Video(models.Model):
    file = models.FileField(upload_to='video/%y')
    title = models.CharField(max_length=5000, default='default')
    thumbnail = models.ImageField(max_length=100, blank=True, null=True)
    views = models.IntegerField(default=0, blank=True, null=True)
    description = models.CharField(max_length=9999, blank=True, null=True)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)   
    category = models.CharField(max_length=16, choices=CATEGORIES, blank=True, null=True)
    create_at = models.DateTimeField(default=timezone.now, blank=True)
    # created_by = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return self.title