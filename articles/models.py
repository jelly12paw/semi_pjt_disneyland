from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Review(models.Model):
    di_names = [      
        ('Los Angeles', 'Los Angeles'),
        ('Paris', 'Paris'),
        ('Tokyo', 'Tokyo'),
        ('Hong Kong', 'Hong Kong'),
    ]
    disney_name = models.CharField('🏰 방문한 디즈니랜드', max_length=20, choices=di_names)
    content = models.TextField('✍🏻 후기 작성')
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    visited_at = models.DateField('📆 방문 날짜', null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    image = ProcessedImageField(upload_to='images/', blank=True,
                            processors=[ResizeToFill(1200, 960)],
                            format='JPEG',
                            options={'quality': 80})

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField('댓글을 작성해주세요!')
    created_at = models.DateTimeField(auto_now_add=True)