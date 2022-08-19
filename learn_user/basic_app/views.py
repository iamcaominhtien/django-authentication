from django.shortcuts import render
from basic_app.forms import UserForm,UserFrofileInfoForm
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    context_dict={
        'title':'Trang chủ'
    }

    return render(request,'basic_app/index.html',context=context_dict)

def registration(request):
    registered=False
    user_form = UserForm()
    profile_form = UserFrofileInfoForm()
    
    if request.method=='POST':
        user_form=UserForm(request.POST)
        profile_form = UserFrofileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            try:
                user = user_form.save()
                user.set_password(user.password)
                user.save()

                profile = profile_form.save(commit=False)
                profile.user=user

                if 'profile_pic' in request.FILES:
                    profile.profile_pic = request.FILES['profile_pic']
                    # im = Image.open(request.FILES['profile_pic'])
                    # im.save() 

                profile.save()

                registered=True
                user_form = UserForm()
                profile_form = UserFrofileInfoForm()
            except NameError:
                print(NameError)

        else:
            print(user_form.errors,profile_form.errors)

    context_dict={
        'title':'Đăng kí',
        'user_form' :user_form,
        'profile_form':profile_form,
        'registered':registered,
    }

    return render(request,'basic_app/registration.html',context=context_dict)

def user_login(request):
    if request.method=='POST':
        print('Iam here ',request)
        username=request.POST.get('username')
        password=request.POST.get('password')
        rememberMe=request.POST.get('rememberMe')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                if not rememberMe:
                    # <-- Here if the remember me is False, 
                    # that is why expiry is set to 0 seconds. 
                    # So it will automatically close the session after the browser is closed.
                    request.session.set_expiry(0)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT IS ACTIVE")
        else:
            print('Login Failed')
            return HttpResponse("Login failed")

    context_dict={
        'title':'Đăng nhập',
        # 'user':user,
    }
    
    return render(request,'basic_app/login.html',context=context_dict)

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def user_logout(request):
    print("Log out")
    logout(request)

    return HttpResponseRedirect(reverse('index'))