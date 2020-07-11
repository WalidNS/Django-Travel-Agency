from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.shortcuts import redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.password_validation import validate_password
from django import forms



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        erro = {'error_message': [] }
        
        if password1==password2:
            try:
                validate_password(password1)
            except forms.ValidationError as e:
                if len(e.messages) > 1:
                    for er in e.messages:
                        erro['error_message'].append(er)
                else:
                    erro['error_message'].append(e.messages)
            if User.objects.filter(username=username).exists():
                erro['error_message'].append('The username is already taken.')
            elif User.objects.filter(email=email).exists():
                erro['error_message'].append('The username is already taken.')
            else:
                user= User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                return redirect('/Home/')
        else:
            erro['error_message'].append('Password do not match.')
        
        return JsonResponse(erro)
    
    else:
        return render(request, 'base.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/Home/')
        else:
            return JsonResponse({'error_message': 'Wrong credentials!'})
    else:
        return render(request, 'base.html')


def logout(request):
    auth.logout(request)
    return redirect('/Home/')
