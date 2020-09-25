from django.contrib import admin


# Register your models here.
from home.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'status', 'create_at')
    list_filter = ('status', 'create_at')

admin.site.site_title = "Mysite1 Admin Panel"
admin.site.site_header ="mysite1 Admin Panel"
admin.site.index_title ="mysite1 Admin Panel Home"

admin.site.register(Contact, ContactAdmin)


