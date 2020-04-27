from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    return render(request,'home/home.html')
def about(request):
    return HttpResponse('this is about')
def contact(request):
    
    
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        content=request.POST['contain']
        
        if(len(name)>2 and len(phone)>9 and len(email)>3 and len(content)>4):
            c=Contact(name=name,phone=phone,email=email,content=content)
            c.save()
            messages.success(request, 'your message has been sent!')
        else:
            messages.error(request, 'please fill the form correctly.')
    return render(request,'home/contact.html')

def search(request):
    query = request.GET['query']
    if len(query)>78:
        allposts = Post.objects.none()
    else:
    # allposts = Post.objects.all()
        allpostsTitle = Post.objects.filter(title__icontains=query)
        allpostsContent = Post.objects.filter(content__icontains=query)
        allposts=allpostsTitle.union(allpostsContent)
    if len(allposts)==0:
        messages.warning(request, 'No search results found. Please refine your query.')
    params={'allposts':allposts,'query':query}
    # print(params)
    return render (request,'home/search.html',params)
    # return HttpResponse("This is search")


def handleSignup(request):
    if request.method == "POST":
        # Get the bost parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2= request.POST['password2']
        
        #Check for error neous inputs
        # username must be less then 10 word
        if len(username) > 10:
            messages.error(request,"username must be less then 10 word")
            return render(request,'home/home.html')
        # username should only contain letters and numbers
        if not username.isalnum():
            messages.error(request,"username should only contain letters and numbers")
            return render(request,'home/home.html')
        # password do not match
        if password1 != password2 :
            messages.error(request,"password do not match")
            return render(request,'home/home.html')





        # create the user
        myuser = User.objects.create_user(username,email,password1)
        myuser.first_name = fname 
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"your account has been successfully created")
        return render(request,'home/home.html')


    else:
        return HttpResponse("404 - Not Found")



def handleLogin(request):
    if request.method == "POST":
        # Get the bost parameters
        loginusername = request.POST[ 'loginusername' ]
        loginpassword = request.POST[ 'loginpassword' ]
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request, "Successfully logged in")
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials, Please try again")
            return redirect('home')
    return HttpResponse("404 - Not Found")

def handleLogout(request):
        logout(request)
        messages.success(request, "Successfully logout")
        return redirect('home')
    
   


    

        