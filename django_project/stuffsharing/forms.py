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
         fields = ('Name','phone','address')

class SearchForm(forms.Form):
	search=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class': "form-control form-control-lg form-control-borderless",'type':"Search",'placeholder':"Search stuffs or keywords"}))
	
class MyAdsAddForm(forms.Form):
	tags = forms.CharField(label = 'Item tags:', max_length=1000,widget=forms.TextInput(attrs={'class': "form-control",'type':"Name",'placeholder':"tag1,tag2,..."}))
	name=forms.CharField(label = 'Item name:', max_length=1000,widget=forms.TextInput(attrs={'class': "form-control",'type':"Name",'placeholder':"name"}))
	description = forms.CharField(label = 'Item Desctiption:', widget=forms.Textarea(attrs={'class': "form-control", 'rows':'3','type':"Description",'placeholder':"item description"}))
	pic1 = forms.FileField(label = '', required=False)
	pic2 = forms.FileField(label = '', required=False)
	pic3 = forms.FileField(label = '', required=False)
	
class MyAdsInactiveForm(forms.Form):
	stuff_for_lown=forms.IntegerField()
	#adName=forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control",'type':"Name",'placeholder':"Ad name"}), required=False)
	start_date=forms.DateField(label = 'Pick up date:', required=False,widget=forms.widgets.SelectDateWidget())
	end_date=forms.DateField(label = 'Return date:', required=False,widget=forms.widgets.SelectDateWidget())
	price=forms.FloatField(label = 'Price', required=False)
	pickupAddress=forms.CharField(label='Address',max_length=255, required=False)
	returnAddress=forms.CharField(label='Address',max_length=255, required=False)
	bid=forms.BooleanField(label='Bidding allowed',initial=False, required=False)
	selectType=forms.ChoiceField(label='Selection', choices=[('auto','automatic'),('manual','manual')], widget=forms.RadioSelect,required=False)
	submitter=forms.CharField()
	
	def clean(self):
		cleaned_data = super().clean()
		if cleaned_data['submitter']=='Post':
			for field in cleaned_data:
				if not field:
					raise forms.ValidationError("All fields are required to create a new add")
		return cleaned_data

class MyAdsActiveBidForm(forms.Form):
	loan_request_id=forms.IntegerField()
	submitter=forms.CharField()

class MyAdsActiveAdForm(forms.Form):
	loan_prop_id=forms.IntegerField()
	submitter=forms.CharField()