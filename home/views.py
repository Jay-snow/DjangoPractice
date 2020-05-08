from django.shortcuts import render, redirect

# Create your views here.

def home(request):

    #Get user
    user = request.user

    #If user is not logged in, redirect them to login page
    if user.is_active is False:
        return redirect('login')
    else:
        #If user is logged in, render the home page.
        return render(request, 'home/index.html')