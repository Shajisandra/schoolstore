from django.shortcuts import render,redirect
from django . http import HttpResponse
from .models import school
from django.contrib.auth.models import User
from django.contrib import messages,auth
# Create your views here.
def index(request):

    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        error_message=None


    #     if password == cpassword:
    #         user=User.objects.create_user(username=username,password=password)
    #         user.save()
    #         messages.success(request, "user created")
    #         return redirect('login')
    #     else:
    #         messages.warning(request, "passwords not matching")
    # return render(request,'register.html')



        if User.objects.filter(username=username).exists():
            messages.warning(request, "username already taken,register by new one")
            return redirect('register')
        else:
            if password == cpassword:
                user = User.objects.create_user(username=username,
                                                password=password)
                user.save()
                messages.success(request, "user created successfully")
                return redirect('login')
            else:
                print("password doesnot matching")
    return render(request, 'register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/welcome')
        else:
            messages.warning(request, "invalid credentials")
            return redirect('login')

    return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def welcome(request):
    return render(request,'welcome.html')
def apply(request):
    if request.method =="POST":
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        mail = request.POST['mail']
        address = request.POST['address']
        department = request.POST['department']
        purpose = request.POST['purpose']
        materials = request.POST['materials']

        error_message= None
        if not name:
            error_message="Name is required"
        elif name:
            if len(name) < 4:
                error_message="Name must be 4 charecters long"
        elif school.objects.filter(mail=mail).exists():
            messages.warning(request, "email already taken,register by new one")
            return redirect('apply')
        if not error_message:

            Schools = school(name=name, dob=dob,age=age,gender=gender,phone=phone,
                                             mail=mail,address=address,department=department,purpose=purpose,materials=materials
                                             )
            Schools.save()
            return render(request,'msg.html')
            return redirect('/')

        else:
             return render(request,'apply.html',{'error':error_message})
        return redirect('/')

    return render(request, "apply.html")


    # return render(request, "apply.html")
# def apply(request):
#     if request.method == "POST":
#         forms = (request.POST)
#
#         if forms.is_valid():
#             forms.save()
#         messages.success(request, "Student Registration Successfully!")
#         return redirect("student_list")
#     else:
#         forms = Createuser()
#
#     context = {
#         "forms": forms
#     }
#     return render(request, "students/registration.html", context)
import re
def validateEmail(mail):
    if len(mail) > 6:
        if re.match('\b[\w\.-]+@[\w\.-]+\. \w{2,4}\b',mail) !=None:
            return 1
        return 0