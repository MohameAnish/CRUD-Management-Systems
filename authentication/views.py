from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout 

# Create your views here.
def LoginPage(request):
     context={'error':''}
     if request.method == 'POST':
          user=authenticate(username=request.POST['username'], password=request.POST['password'])
          if user is not None:
               login(request, user)
               return render(request,'customer_add.html')
          else:
               context={'error':'Invalid username or password'}
               return render(request, 'login.html', context)
     return render(request, 'login.html')

def LogoutPage(request):
     logout(request)
     return render(request, 'login.html')
     if request.method == 'POST':
          logout(request)
          return redirect('login')

