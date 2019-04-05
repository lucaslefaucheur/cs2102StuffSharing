from django.contrib import admin
from .models import Adress, Profile, Stuff, LoanProposition, LoanRequest, Loan
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(Adress)
admin.site.register(Profile)
admin.site.register(Stuff)
admin.site.register(LoanProposition)
admin.site.register(LoanRequest)
admin.site.register(Loan)