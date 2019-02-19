from django.db import models

# Create your models here.

class TestUser(models.Model): 
    name = models.CharField(max_length=255, primary_key=True)

class TestObject(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    
class IsWillingToRent(models.Model):
    testuser = models.ForeignKey(TestUser, on_delete=models.CASCADE)
    testobject = models.ForeignKey(TestObject, on_delete=models.CASCADE)
