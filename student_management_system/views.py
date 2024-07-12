from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from app.models import CustomUser

def home(request):
    return render(request,'home.html')

def Login(request):
    if request.method == "POST":
        email = request.POST['Email']
        password = request.POST['Password']
        user = authenticate(request,username=email,password=password)
        if user is not None:
            login(request,user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                return redirect('staff_home')
            elif user_type == '3':
                return redirect('student_home')
            else:
                return redirect('home')
        else:
            messages.success(request,'Incorrect password or username')
            return redirect('login')
    return render(request,'login.html')

def Logout(request):
    logout(request)
    return redirect('login')

def profile(request):
    user = CustomUser.objects.get(id = request.user.id)
    return render(request,'profile.html',{'user':user})

def profile_update(request):
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        profile_pic = request.FILES['profile_pic']
        print(profile_pic)
        try:
            user = CustomUser.objects.get(id=request.user.id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            if password!=None and password != "":
                user.set_password(password)
            if profile_pic != None and profile_pic != "":
                user.profilepic = profile_pic
            user.save()
            messages.success(request,'profile updated successful')
            return redirect('login')
        except:
            messages.success(request,'Failed to update..')
    return render(request,'profile.html')


