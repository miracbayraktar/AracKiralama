from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactFormMessage, UserProfil


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name','email', 'subject','message','status']
    list_filter = ['status']

class UserProfilAdmin(admin.ModelAdmin):
    list_display = ['user_name','city','country', 'address','image_tag']


admin.site.register(ContactFormMessage,ContactFormMessageAdmin)
admin.site.register(Setting)
admin.site.register(UserProfil,UserProfilAdmin)
