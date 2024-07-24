from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm, CreateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import record
# Create your views here.

      #home page
def home(request):
    return render(request, 'crmapp/index.html', {'name': 'Siddharth'})



   #Register

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    context = {'form': form}    
    return render(request, 'crmapp/register.html', context)

# login a user

def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Loged in successfully')
                return redirect('dashboard')
    context = {'form': form}
    return render(request,'crmapp/my-login.html',context )
    

  # logout a user

def user_logout(request):
    logout(request)
    messages.success(request, 'Loged out successfully!')
    return redirect('user_login')




    #.... Dashboard.....#
@login_required(login_url='user_login')
def dashboard(request):
    customer_data = record.objects.all()
    context = {'customer_data':customer_data}
    return render(request, 'crmapp/dashboard.html', context)



# .....ADDING RECORD.....

def addRecord(request):
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'crmapp/create-record.html', context)


# .... UPDATE RECORD.....

@login_required(login_url='user_login')
def updateRecord(request, pk):
    customer_data = record.objects.get(id=pk)
    form = CreateRecordForm(instance=customer_data)
    if request.method == 'POST':
        form = CreateRecordForm(request.POST, instance=customer_data)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'crmapp/update-record.html', context)



#...... Read and View a single Record......

@login_required(login_url='user_login')
def viewRecord(request, pk):
    customer_data = record.objects.get(id=pk)
    context = {'customer_data':customer_data}
    return render(request, 'crmapp/view-record.html', context)


#......DELETE RECORD...........
@login_required(login_url='user_login')
def deleteRecord(request, pk):
    customer_data = record.objects.get(id=pk)
    customer_data.delete()
    return redirect('dashboard')



