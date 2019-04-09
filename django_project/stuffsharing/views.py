from django.shortcuts import render,redirect
from stuffsharing.models import  Profile, Stuff, LoanProposition, LoanRequest
from .forms import SearchForm
from .forms import SignUpForm
from .forms import UserProfileInfoForm
from .forms import MyAdsAddForm
from .forms import MyAdsInactiveForm
from .forms import MyAdsActiveBidForm
from .forms import MyAdsActiveAdForm
from django.db import connection
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
	if request.user.is_authenticated :
		if request.method=='POST':
			form=MyAdsAddForm(request.POST)
			if form.is_valid():
				t=form.cleaned_data['tags']
				d=form.cleaned_data['description']
				o=request.user.profile
				s=Stuff(tags=t,description=d,owner=o)
				s.save()
				
	form=MyAdsAddForm()
	return render(request, 'stuffsharing/myadsadd.html', {'form': form})

def myadsactive(request):
	if request.user.is_authenticated :
		o=request.user.profile
		if request.method=='POST':
			if request.POST['submitter'] == 'remove':
				form=MyAdsActiveAdForm(request.POST)
				if form.is_valid():
					p_id = form.cleaned_data['loan_prop_id']
					with connection.cursor() as cursor:
						cursor.execute("DELETE FROM stuffsharing_loanproposition WHERE id = %s",[p_id])
					#LoanProposition.objects.raw("SELECT * FROM stuffsharing_loanproposition WHERE id = %s",[p_id]).delete()
			else:
				form=MyAdsActiveBidForm(request.POST)
				if form.is_valid():
					r_id = form.cleaned_data['loan_request_id']
					if form.cleaned_data['submitter']=='accept':
						lreq = LoanRequest.objects.raw('SELECT * FROM stuffsharing_loanrequest WHERE id = %s',[r_id])[0]
						lreq.accepted=True
						lreq.save()
						lprop = lreq.original_proposition
						lprop.available=False
						lprop.save()
						newloan = Loan(loan=lreq)
						newloan.save()
					else:
						with connection.cursor() as cursor:
							cursor.execute("DELETE FROM stuffsharing_loanrequest WHERE id = %s",[r_id])
						#LoanRequest.objects.raw('SELECT * FROM stuffsharing_loanrequest WHERE id = %s',[r_id]).delete()
		
		propsList=LoanProposition.objects.raw("SELECT * FROM stuffsharing_loanproposition WHERE owner_id = %s",[o.user_id])
		if len(propsList) > 0:
			propsAndForms=[]
			for prop in propsList:
				lrequests=LoanRequest.objects.raw('SELECT * FROM stuffsharing_loanrequest WHERE original_proposition_id = %s',[prop.id])
				reqAndForm=[]
				for req in lrequests:
					reqAndForm.append((req, MyAdsActiveBidForm(initial={'Loan_request_id': req.id})))
				propsAndForms.append((prop, MyAdsActiveAdForm(initial={'loan_prop_id': prop.id}), reqAndForm))
			return render(request, 'stuffsharing/myadsactive.html', {'propsAndForms': propsAndForms})
		else:
			return render(request, 'stuffsharing/myadsactive.html')
	else:
		return render(request, 'stuffsharing/myadsactive.html')

def myadsinactive(request):
	if request.user.is_authenticated :
		o=request.user.profile
		if request.method=='POST':
			form=MyAdsInactiveForm(request.POST)
			if form.is_valid():
				if form.cleaned_data['submitter']=='Delete':
					sid = form.cleaned_data['stuff_for_lown']
					with connection.cursor() as cursor:
							cursor.execute("DELETE FROM stuffsharing_stuff WHERE id = %s",[sid])
					#Stuff.objects.raw('SELECt * FROM stuffsharing_stuff WHERE id = %s',[sid]).delete()
				else:
					sid = form.cleaned_data['stuff_for_lown']
					aname = form.cleaned_data['adName']
					sdate = form.cleaned_data['start_date']
					edate = form.cleaned_data['end_date']
					pr=form.cleaned_data['price']
					paddr = form.cleaned_data['pickupAddress']
					raddr = form.cleaned_data['returnAddress']
					b=form.cleaned_data['bid']
					stuff = Stuff.objects.raw('SELECT * FROM stuffsharing_stuff WHERE id = %s',[sid])[0]
					newloanprop=LoanProposition(owner=o,name=aname,stuff_for_lown=stuff, start_date=sdate,end_date=edate,price=pr,pickupAdress=paddr,returnAdress=raddr,available=True,bid=b)
					newloanprop.save()
				
		inactiveStuff = Stuff.objects.raw('SELECT * from stuffsharing_stuff S WHERE owner_id = %s AND NOT EXISTS(SELECT 1 FROM stuffsharing_LoanProposition WHERE stuff_for_lown_id = S.id)', [o.user_id])
		if len(inactiveStuff)!=0:
				propForms=[]
				for item in inactiveStuff:
					#propForms.append({'stuff': item, 'form': MyAdsInactiveForm(initial={'stuff_for_lown': item.id})})
					propForms.append((item, MyAdsInactiveForm(initial={'stuff_for_lown': item.id,'pickupAddress': o.address, 'returnAddress': o.address})))
				return render(request, 'stuffsharing/myadsinactive.html', {'formList': propForms})
				
	return render(request, 'stuffsharing/myadsinactive.html')

def about(request):
    return render(request, 'stuffsharing/about.html')

def myrequests(request):
    return render(request, 'stuffsharing/myrequests.html')

def currenttransactions(request):
    return render(request, 'stuffsharing/currenttransactions.html')

def myaccount(request):
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
        	#profile.user_name=form.cleaned_data['Name']
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



    