from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
# from .models import User
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):

    username = forms.CharField(
    label ='아이디',
    widget=forms.TextInput(attrs={
        'placeholder' : '아이디'
    }))

    TITLE_CHOICES = [      
        ('남성', '남성'),
        ('여성', '여성'),
        ]

    gender = forms.ChoiceField(
        label='성별',
        choices=TITLE_CHOICES
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'gender')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)

class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label ='아이디',
        widget=forms.TextInput(attrs={"autofocus": True}))