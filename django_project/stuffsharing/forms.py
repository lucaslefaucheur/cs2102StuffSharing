from django import forms


class SearchForm(forms.Form):
	search=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class': "form-control form-control-lg form-control-borderless",'type':"Search",'placeholder':"Search stuffs or keywords"}))