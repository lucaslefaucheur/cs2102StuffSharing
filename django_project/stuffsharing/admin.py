from django.contrib import admin
from .models import Adress, Member, Stuff, LoanProposition, LoanRequest, Loan

# Register your models here.
admin.site.register(Adress)
admin.site.register(Member)
admin.site.register(Stuff)
admin.site.register(LoanProposition)
admin.site.register(LoanRequest)
admin.site.register(Loan)