from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from stuffsharing.models import Profile


class SignUpForm(UserCreationForm):
  
    class Meta:
        model = User
        fields = ('username','email')
       
class UserProfileInfoForm(forms.ModelForm):
	
     class Meta():
         model = Profile
         fields = ('user_name','phone','address')

class SearchForm(forms.Form):
	search=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class': "form-control form-control-lg form-control-borderless",'type':"Search",'placeholder':"Search stuffs or keywords"}))