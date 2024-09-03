from django import forms
from .models import Todo,User


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        #fields = "__all__"
        fields = ('title', 'details','image','date')

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password','image')