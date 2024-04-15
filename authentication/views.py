from decimal import Decimal
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import BankAccount, Transaction
from authentication import admin
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    return render(request,"home_page/index.html")

def signup(request):
    if request.method == "POST":
        username=request.POST["username"]
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']


        if password==confirm_password:   
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect('signup')
            else:         
                user = User.objects.create_user(username=username, password=password, 
                                        email=email, first_name=fname, last_name=lname)
                # user1= admin(admin_id=user.id,admin_name=fname,admin_email=email)
                # user1.save()
                user.save()
                login(request,user)                
                return redirect('home')
        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect('signup')
            

    else:
        return render(request, 'authentication/signup.html')    
    
@csrf_exempt
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)     

            return redirect('home')
        # return render(request, 'home_page/index.html')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('signin')
    else:
        return render(request, 'authentication/signin.html')

def signout(request):
    logout(request)
    return redirect('home')

@login_required
def deposit(request):
    account, created = BankAccount.objects.get_or_create(owner=request.user)
    if request.method == 'POST':
        amount = Decimal(request.POST.get('amount'))
        # account = BankAccount.objects.get(owner=request.user)
        account.deposit(amount)
        return redirect('balance')
    return render(request,'authentication/deposit.html')

@login_required
def withdraw(request):
    account, created = BankAccount.objects.get_or_create(owner=request.user)
    if request.method == 'POST':
        amount = Decimal(request.POST.get('amount'))
        # account = BankAccount.objects.get(owner=request.user)
        if account.withdraw(amount):
            return redirect('balance')
        else:
            message = "Insufficient balance"
            return render(request, 'authentication/withdraw.html', {'message': message})
    return render(request, 'authentication/withdraw.html')

@login_required
def balance(request):
    account, created = BankAccount.objects.get_or_create(owner=request.user)
    # account = BankAccount.objects.get(owner=request.user)
    balance = account.get_balance()
    return render(request, 'authentication/balance.html', {'balance': balance})

@login_required
def transaction_report(request):
    transactions = Transaction.objects.filter(account__owner=request.user)
    return render(request, 'authentication/transaction_report.html', {'transactions': transactions})