from django.shortcuts import render, redirect

from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.
#def index(request):
    #total_users = User.objects.count()
    #return render(request, "index.html", {'UserCount':total_users})

def register(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        #last_name = request.POST['last_name']
       # username = request.POST['username']
        email = request.POST['email']
        city = request.POST['city']
        mobile_number = request.POST['mobile_number']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            #if User.objects.filter(username=username).exists():
               # messages.info(request, 'Username Taken')
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Id already registered')
            else:

                user = User.objects.create_user( password=password1, email=email, full_name=full_name,city=city, mobile_number=mobile_number )
                user.save();

                #messages.info(request, 'User Created')
                messages.success(request, 'User Created')
                return render(request,'index.html')
                return redirect('index')

        else:
            messages.info(request, 'Password Not Matching..')
            return redirect('/')
    else:
        return render(request, '/')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Invalid Login credentials')
            return redirect('/')

    else:
        return render(request, '/')

def logout(request):
    auth.logout(request)
    return redirect('/')
