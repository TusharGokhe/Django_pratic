from django.contrib import admin
from app1.models import Student # ye file ko import kar diya
from app1.models import File_Data  #uplaod file import
# Register your models here. 

class StudentAdmin(admin.ModelAdmin):   # ye sari name/objets ko print kar dega
    list_display =['st_name','st_email','st_phone']


# Student ko register kiy hai

admin.site.register(Student,StudentAdmin)

admin.site.register(File_Data)
