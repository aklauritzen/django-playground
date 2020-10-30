from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# Create your views here.
from .forms import LoginForm, RegisterForm

User = get_user_model()

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")

        try:
            user = User.objects.create_user(username, email, password)
        except:
            user = None
        if user != None:
            login(request, user)
            return redirect("/")
        else:
            request.session['register_error'] = 1
        
    return render(request, "forms.html", {"form": form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
    
        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Authenticate checks if the username and password is correct
            user = authenticate(request, username=username, password=password)

            if user != None:
                # User is valid and active -> is_active
                # request.user == user
                login(request, user)
                
                # Login succes redirect
                return redirect("/")
            else:                  
                # Todo: Count number of login attempts
                request.session['invalid_user'] = 1  # 1 == True
                            
    else:
        # If form is empty
        form = LoginForm()
        
    
    return render(request, "forms.html", {"form": form})


def logout_view(request):
    logout(request)    
    return redirect("/login")