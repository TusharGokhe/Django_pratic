from django.db import models

# Create your models here.
class Student(models.Model):

    st_name = models.CharField(max_length=50,null=True)
    st_email = models.EmailField(max_length=50,null=True)
    st_phone= models.IntegerField(null=True)
    img = models.ImageField(null=True)

    def __str__(self):
        return self.st_name
    
class File_Data(models.Model):    # upload files  us ke baad me admin me resgiter karn hoga data me save krn ke liya
    files = models.FileField(upload_to='data')  #uplod_to ka use apn scirate folder ka ander file save kr sakte hia 


# models baane ke baad jayega apn admin.py file ka ander  import karn  and resiter karn ka liya