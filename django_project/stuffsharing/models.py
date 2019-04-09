from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
# Create your models here.


class Adress(models.Model):
	adress_name=models.CharField(max_length=255,default='',primary_key=True)
	area=models.CharField(max_length=255)

class Profile(models.Model): 
	
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	#name = models.CharField(max_length=255)
	user_name = models.CharField(max_length=255,unique=False)
	#mail = models.CharField(max_length=255)
	phone = models.CharField(max_length=12)
	adress= models.CharField(max_length=1000,default='')



class Stuff(models.Model):
	owner=models.ForeignKey(Profile,to_field='user_id',on_delete=models.CASCADE)
	description=models.CharField(max_length=255,default='')
	tags=models.CharField(max_length=1000,default='')
	image=models.CharField(max_length=1000,default='')


class LoanProposition(models.Model):
	owner=models.ForeignKey(Profile,to_field='user_id',on_delete=models.CASCADE,default='')
	name=models.CharField(max_length=255,default='')
	stuff_for_lown=models.ForeignKey(Stuff,on_delete=models.CASCADE)
	start_date=models.DateField('Data available')
	end_date=models.DateField('Data end return')
	price=models.FloatField(default=0.0)
	pickupAdress=models.CharField(max_length=1000,default='')
	returnAdress=models.CharField(max_length=1000,default='')
	available=models.BooleanField(default=True)
	bid=models.BooleanField(default=False)
	



class LoanRequest(models.Model):
    original_Proposition = models.ForeignKey(LoanProposition, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Profile,to_field='user_id', on_delete=models.CASCADE)
    accepted=models.BooleanField(default=False)
    price=models.FloatField()
'''
class Loan(models.Model):
	loan=models.ForeignKey(LoanRequest,on_delete=models.CASCADE)
	status=models.BooleanField(default=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''
'''@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()'''
    #signals.post_save.connect(create_user_profile, sender=User)

