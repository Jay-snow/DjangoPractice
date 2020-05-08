from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.

def login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']

            get_all = User.objects.all()
            print(get_all)
            print(user_name)
            print(password)

            user = authenticate(user_name='marcus', password='t3rranImba')

            print(user)

            if user is not None:
                #  User exists
                print('success')
                return redirect('success')
            else:
                # User is not authenticated on backend
                print('sorry pal')
    else:
        form = LoginForm()


    return render(request, 'login/index.html', {'form': form})


def success(request):

    return render(request, 'login/success.html')
