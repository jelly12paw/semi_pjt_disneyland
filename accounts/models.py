from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class User(AbstractUser):
    TITLE_CHOICES = [      
        ('남성', '남성'),
        ('여성', '여성'),
        ]
    gender = models.CharField(max_length=3,choices=TITLE_CHOICES)
    followings = models.ManyToManyField('self', symmetrical=False, related_name = 'followers')
    


class Profile(models.Model):
    image = models.ImageField(upload_to="", default='캡처.jpg')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)