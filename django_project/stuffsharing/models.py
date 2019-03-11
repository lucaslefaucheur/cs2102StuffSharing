from django.db import models

# Create your models here.


class Adress(models.Model):
	adress_name=models.CharField(max_length=255,primary_key=True)
	area=models.CharField(max_length=255)

class Member(models.Model): 
    name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255, primary_key=True)
    mail = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    adress= models.ForeignKey(Adress,on_delete=models.CASCADE)



class Stuff(models.Model):
	owner=models.ForeignKey(Member,on_delete=models.CASCADE)
	description=models.CharField(max_length=255,default='')
	tags=models.CharField(max_length=1000,default='')


class LoanProposition(models.Model):
	stuff_for_lown=models.ForeignKey(Stuff,on_delete=models.CASCADE)
	start_date=models.DateField('Data available')
	end_date=models.DateField('Data end return')
	price=models.FloatField()
	pickupAdress=models.ForeignKey(Adress,on_delete=models.CASCADE,related_name='pickupAdress')
	returnAdress=models.ForeignKey(Adress,on_delete=models.CASCADE,related_name='returnAdress')
	available=models.BooleanField(default=True)
	tags=models.CharField(max_length=1000,default='')



class LoanRequest(models.Model):
    original_Proposition = models.ForeignKey(LoanProposition, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Member, on_delete=models.CASCADE)
    accepted=models.BooleanField(default=False)
    price=models.FloatField()

class Loan(models.Model):
	loan=models.ForeignKey(LoanRequest,on_delete=models.CASCADE)
	status=models.BooleanField(default=True)
