from django.contrib import admin
from .models import Adress, Profile, Stuff, LoanProposition, LoanRequest, Loan
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile


# Register your models here.
admin.site.register(Adress)
admin.site.register(Profile)
admin.site.register(Stuff)
admin.site.register(LoanProposition)
admin.site.register(LoanRequest)
admin.site.register(Loan)

class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False
	verbose_name_plural = 'Profile'
	fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)