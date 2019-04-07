from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Adress(models.Model):
	adress_name=models.CharField(max_length=255,primary_key=True)
	area=models.CharField(max_length=255)

class Profile(models.Model): 
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	user_name = models.CharField(max_length=255, primary_key=True)
	mail = models.CharField(max_length=255)
	phone = models.CharField(max_length=12)
	adress= models.ForeignKey(Adress,on_delete=models.CASCADE)



class Stuff(models.Model):
	owner=models.ForeignKey(Profile,on_delete=models.CASCADE)
	description=models.CharField(max_length=255,default='')
	tags=models.CharField(max_length=1000,default='')
	image=models.CharField(max_length=1000,default='')


class LoanProposition(models.Model):
	owner=models.ForeignKey(Profile,on_delete=models.CASCADE,default='')
	name=models.CharField(max_length=255,default='')
	stuff_for_lown=models.ForeignKey(Stuff,on_delete=models.CASCADE)
	start_date=models.DateField('Data available')
	end_date=models.DateField('Data end return')
	price=models.FloatField()
	pickupAdress=models.ForeignKey(Adress,on_delete=models.CASCADE,related_name='pickupAdress')
	returnAdress=models.ForeignKey(Adress,on_delete=models.CASCADE,related_name='returnAdress')
	available=models.BooleanField(default=True)
	bid=models.BooleanField(default=False)
	



class LoanRequest(models.Model):
    original_Proposition = models.ForeignKey(LoanProposition, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Profile, on_delete=models.CASCADE)
    accepted=models.BooleanField(default=False)
    price=models.FloatField()

class Loan(models.Model):
	loan=models.ForeignKey(LoanRequest,on_delete=models.CASCADE)
	status=models.BooleanField(default=True)
'''
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
