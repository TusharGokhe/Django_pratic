from django.shortcuts import render
from django.http import HttpResponse
from app1.forms import StudentForm   #forms ko importe karega 
from .models import Student
from .models import File_Data #upload files import

# Create your views here.

def home(req):
    my_data = Student.objects.all()
    if req.method == "POST":
        data = StudentForm(req.POST,req.FILES)
        if(data.is_valid()):
            data.save()      #form store hoga yaha per
    
    stu_form = StudentForm() 
    
    context = {
        "form" :  stu_form,
        "data": my_data

    }
    return render(req,"home.html",context)

def save_form (req):
    if req.method == "POST":
        form = StudentForm(req.POST)
        if(form.is_valid()):
            form.save()
    
    return HttpResponse("helo world")


# def save_file(request):
#     if request.method == 'POST':
#         a = request.FILES['file']
#         my_data = File_Data.objects.create(files = a)   #database me save hogi file 
#         my_data.save()
#         print(a)
#     return HttpResponse("Upload file")








def Contact(req):
    dict ={"name":"abhay",
           "age":49,
           "cars":['tushar','pyush','rohit','abhay']
           
           }
    return render(req,"contact.html",dict)





def courses(req,id):  # ID get karne ka liya 
    return HttpResponse(id)

def abhay(req,data):    # Str  data get karn ka liya
    return HttpResponse(data)