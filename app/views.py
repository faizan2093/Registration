from django.shortcuts import render
from . models import *
# Create your views here.

#View for registration Page
def RegisterPage(request):
    return render(request,"app/registration.html")

#View For user registration 
# def UserRegister(request):
#     if request.method == "POST":
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#         contact = request.POST['contact']
#         password = request.POST['password']
#         cpassword = request.POST['cpassword']

#         #first we will validate that user already exist
#         user = User.objects.filter(Email = email)

#         if user:
#             message = "User Already Exist"
#             return render(request, "app/login.html",{'msg':message})
#         else:
#             if password == cpassword:
#                 newuser = User.objects.create(Firstname = fname, Lastname = lname, Email = email, Contact = contact, Password = password)
#                 message = "User Register Successfully"
#                 return render(request,"app/login.html",{'msg':message})
#             else:
#                 message = "Password and Conform Password Does Not Match! "
#                 return render(request, "app/registration.html",{'msg':message})

def UserRegister(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        # Check if a user with the given email already exists
        if User.objects.filter(Email=email).exists():
            message = "User Already Exist"
            return render(request, "app/registration.html", {'msg': message})
        else:
            if password == cpassword:
                newuser = User.objects.create(Firstname=fname, Lastname=lname, Email=email, Contact=contact, Password=password)
                message = "User Register Successfully"
                return render(request, "app/login.html", {'msg': message})
            else:
                message = "Password and Conform Password Does Not Match! "
                return render(request, "app/registration.html", {'msg': message})
    else:
        return render(request, "app/registration.html")
    
#login View
def LoginPage(request):
    return render(request,"app/login.html")


#Login User
# def loginUser(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         password = request.POST['password']

#         #checking email id with DATA base
#         user = User.objects.get(Email = email)

#         if user:
#             if user.Password == password:
#                 #we are getting user data in session
#                 request.session['Firstname'] = user.Firstname
#                 request.session['Lastname'] = user.Lastname
#                 request.session['Email'] = user.Email
#                 return render(request,"app/Home.html")
#             else:
#                 message = "Password Does not Match"
#                 return render(request,"app/login.html",{'msh': message})
            
#         else:
#             message = "User does not Exist"
#             return render(request,"app/registratio.html",{'msg':message})

def loginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            # checking email id with DATA base
            user = User.objects.get(Email=email)

            if user.Password == password:
                # we are getting user data in session
                request.session['Firstname'] = user.Firstname
                request.session['Lastname'] = user.Lastname
                request.session['Email'] = user.Email
                return render(request, "app/Home.html")
            else:
                message = "Password Does not Match"
                return render(request, "app/login.html", {'msg': message})

        except User.DoesNotExist:
            message = "User does not Exist"
            return render(request, "app/login.html", {'msg': message})

    else:
        return render(request, "app/login.html")
