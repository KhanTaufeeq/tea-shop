from django.shortcuts import render, redirect
from django.contrib.auth.models import User 

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

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['fname']
        last_name = request.POST['lname'] 
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']

