from django.shortcuts import render
from stuffsharing.models import Adress, Member, Stuff, LoanProposition, LoanRequest, Loan
from .forms import SearchForm
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def home(request):
	if request.method=='POST':
		form=SearchForm(request.POST)
		if form.is_valid():
			search=form.cleaned_data['search']
			
			result=LoanProposition.objects.filter(tags__contains=search)
			print(result)
			if len(result)!=0:
				propositions=[]
				for proposition in result:
					if proposition.available:
						propositions.append(proposition)
				return render(request, 'stuffsharing/search.html', {'form': form,'propositions':propositions})
	else:
		form=SearchForm()
		
	return render(request, 'stuffsharing/home.html', {'form': form})

@csrf_protect
def search(request):
	if request.method=='POST':
		form=SearchForm(request.POST)
		if form.is_valid():
			search=form.cleaned_data['search']
			
			result=LoanProposition.objects.filter(tags__contains=search)
			print(result)
			if len(result)!=0:
				propositions=[]
				for proposition in result:
					if proposition.available:
						propositions.append(proposition)
				return render(request, 'stuffsharing/search.html', {'form': form,'propositions':propositions})
	else:
		form=SearchForm()
		
	return render(request, 'stuffsharing/search.html', {'form': form})

def post(request):
    return render(request, 'stuffsharing/post.html')

def about(request):
    return render(request, 'stuffsharing/about.html')


