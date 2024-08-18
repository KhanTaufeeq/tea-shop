from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
# Create your views here.

# Django uses request and response objects to pass state through the system.

# When a page is requested, Django creates an HttpRequest object that contains metadata about the request. 
# Then Django loads the appropriate view, passing the HttpRequest as the first argument to the view function. 
# Each view is responsible for returning an HttpResponse object.

# HttpRequest.GET
# A dictionary-like object containing all given HTTP GET parameters.

# HttpRequest.POST
# A dictionary-like object containing all given HTTP POST parameters, 
# providing that the request contains form data. 
# If you need to access raw or non-form data posted in the request, 
# access this through the HttpRequest.body attribute instead.

# It’s possible that a request can come in via POST with an empty POST dictionary – if, say, 
# a form is requested via the POST HTTP method but does not include form data. 
# Therefore, you shouldn’t use if request.POST to check for use of the POST method; 
# instead, use if request.method == "POST" (see HttpRequest.method).

# POST does not include file-upload information.

def home(request):
    return render(request, 'index.html',{})

def signup(request):
    if request.method == 'POST':
        print("POST details",request.POST)
        username = request.POST['username']
        first_name = request.POST['fname']
        last_name = request.POST['lname'] 
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2'] 

        if User.objects.filter(username = username).exists():
            messages.error(request, 'User already exists! Please try another user name')
            return redirect('signup') 
        
        if User.objects.filter(email = email).exists():
            messages.error(request, 'This email has already been taken') 
            return redirect('signup')
        
        if len(username) > 20:
            messages.error(request, 'Username must be under 20 characters!') 
            return redirect('signup') 
        
        if password1 != password2:
            messages.error(request, "Passwords did not match")
            return redirect('signup') 
        
        if not username.isalnum():
            messages.error(request, 'Username must be alpha numeric') 
            return redirect('signup') 
        
        myUser = User.objects.create_user(username, email, password1)
        myUser.first_name = first_name
        myUser.last_name = last_name 
        myUser.is_active = False 
        myUser.save() 
        messages.success(request, "Your account has succefully created, Please check your email address to activate your account")
        return render(request, 'signin.html', {})

    return render(request, 'signup.html', {})

        # from django.contrib.auth.models import User
        # u = User.objects.get(username="john")
        # u.set_password("new password")
        # u.save() 
        
def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass1'] 

        user = authenticate(username = username , password = password) 

        if user is not None:
            login(request, user)
            first_name = user.first_name 
            return render(request, 'index.html', {'first_name':first_name}) 
        
        else:
            messages.error(request, 'Bad Credentials!')
            return redirect('signin')
        
    return render(request, 'signin.html', {})


def signout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully!')
    return redirect('home')
