from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactFormMessage


class ContactformAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'status']
    list_filter = ['status']


admin.site.register(ContactFormMessage, ContactformAdmin)
admin.site.register(Setting)