from django.contrib import admin
from beeta.models import User,OTP

class UserAdmin(admin.ModelAdmin):
 list_display=('name','email')
    
admin.site.register(User, UserAdmin)
admin.site.register(OTP)