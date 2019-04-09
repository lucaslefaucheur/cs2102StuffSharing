from django.shortcuts import render,redirect
from stuffsharing.models import Adress, Profile, Stuff, LoanProposition, LoanRequest
from .forms import SearchForm
from .forms import SignUpForm
from .forms import UserProfileInfoForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import uuid
from django.contrib.auth import login, authenticate


@csrf_protect
def home(request):
	if request.method=='POST':
		form=SearchForm(request.POST)
		if form.is_valid():
			search='%'+form.cleaned_data['search']+'%'
			query=LoanProposition.objects.raw('SELECT * FROM stuffsharing_LoanProposition L join stuffsharing_Stuff S on L.stuff_for_lown_id=S.id WHERE S.tags LIKE %s', [search])
			result=[i for i in query]

			if len(result)!=0:
				propositions=[]
				for proposition in result:
					if proposition.available:
						propositions.append(proposition)
				print(propositions)
				print('##################################')
				return render(request, 'stuffsharing/search.html', {'form': form,'propositions':propositions})
	else:
		form=SearchForm()
		
	return render(request, 'stuffsharing/home.html', {'form': form})

@csrf_protect
def search(request):
	if request.method=='POST':
		form=SearchForm(request.POST)
		if form.is_valid():
			search='%'+form.cleaned_data['search']+'%'
			query=LoanProposition.objects.raw('SELECT * FROM stuffsharing_LoanProposition L join stuffsharing_Stuff S on L.stuff_for_lown_id=S.id WHERE S.tags LIKE %s', [search])
			result=[i for i in query]

			if len(result)!=0:
				propositions=[]
				for proposition in result:
					if proposition.available:
						propositions.append(proposition)
				print(propositions)
				print('##################################')
				return render(request, 'stuffsharing/search.html', {'form': form,'propositions':propositions})
	else:
		form=SearchForm()
	return render(request, 'stuffsharing/search.html', {'form': form})


def myadsadd(request):


    return render(request, 'stuffsharing/myadsadd.html')

def myadsactive(request):
    
	return render(request, 'stuffsharing/myadsactive.html')



def myadsinactive(request):
    return render(request, 'stuffsharing/myadsinactive.html')

def about(request):
    return render(request, 'stuffsharing/about.html')

def myrequests(request):
    return render(request, 'stuffsharing/myrequests.html')

def currenttransactions(request):
    return render(request, 'stuffsharing/currenttransactions.html')

def myaccount(request):
	if request.user.is_authenticated :
		loan_list=LoanProposition.objects.filter(owner=request.user.profile)
		return render(request, 'stuffsharing/myaccount.html',{'loans':loan_list})
	else:
		return render(request, 'stuffsharing/myaccount.html')

def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)
        print('checking valid form')
        print('valid',user_form.is_valid())
        if user_form.is_valid() and profile_form.is_valid() :
        
        	user = user_form.save()
        	user.save()
        	profile = profile_form.save(commit=False)
        	profile.user = user
        	profile.save()
        	registered = True
        	if registered : 
        		login(request, user)
        		return redirect('/')
        else:
       		print(user_form.errors,profile_form.errors)
    else:
        user_form = SignUpForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'stuffsharing/signup.html', {'user_form': user_form,'profile_form':profile_form})



    