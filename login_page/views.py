from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def user_login(request):
    if 'name' in request.session:
        return redirect(home)
    user_name = request.POST.get('name')
    pass_word = request.POST.get('pass')
    if request.method == 'POST':
        user = authenticate(username = user_name, password = pass_word)
        if user_name == '':
            user_err_msg = 'Please enter username!!'
            return render(request,'login.html',{ 'msg_item1' :user_err_msg })
        elif pass_word == '' or len(pass_word) < 4:
            pass_err_msg = 'Please enter password!! , Atleast 4 charecters..'   
            return render(request,'login.html',{ 'msg_item2' :pass_err_msg})
        else:
            if user is not None:
                request.session['name'] = user_name
                login(request,user)
                messages.success(request, 'Login successfully!!')
                return redirect(home)
            else:
                messages.error(request, 'User does\'nt exist!! ')
                return redirect(user_login)
    return render(request,'login.html')

def home(request):
    if 'name' in request.session:
         return render(request, 'home.html')
    return redirect(user_login)

def user_logout(request):
    if 'name' in request.session:
        request.session.flush()
        logout(request)
        return redirect(user_login)


