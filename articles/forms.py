from django import forms
from .models import Review, Comment
from django.forms.widgets import DateInput, Textarea, TextInput, FileInput
from imagekit.models import ProcessedImageField


class ReviewForm(forms.ModelForm):

    GRADE_CHOICES = [      
        ('1', '⭐'),
        ('2', '⭐⭐'),
        ('3', '⭐⭐⭐'),
        ('4', '⭐⭐⭐⭐'),
        ('5', '⭐⭐⭐⭐⭐'),
        ]

    grade = forms.ChoiceField(
        label='⭐ 평점',
        choices=GRADE_CHOICES
    )

    class Meta:
        model = Review
        fields = ['disney_name', 'content', 'grade', 'visited_at', 'image']
        widgets = {
            'visited_at': DateInput(attrs={'type': 'date'}),
            'content': Textarea(attrs={'rows':3})
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment 
        fields = ['content',]
        widgets = {
            'content': Textarea(attrs={'rows':1})
        }