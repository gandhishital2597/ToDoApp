from django.contrib import admin

# Register your models here.
from .models import *

class TaskAdmin(admin.ModelAdmin): #inherit the field from models like so see the main admin all this field
    list_display = ('task','is_completed','updated_at')
    search_fields = ('task',)
admin.site.register(Task,TaskAdmin)

#list_display its buy default fields name to see in the django admin add in the admin page
#same as search field : its by defaulkt django admin add in the admin page