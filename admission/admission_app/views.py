from django.shortcuts import render,redirect
from django.http import HttpResponse
from  django.contrib.auth.forms  import  UserCreationForm
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
students = [
    {
        'name': 'John Doe',
        'email': 'john@gmail.com',
        'age': 20,
        'course': 'Computer Science',
        'date_joined': '2021-01-01'
    }
]



def home(request):
    context = {
        'students': students
    }
    application = Application.objects.get(user=request.user)
    return render(request, 'admission_app/home.html', {'contect':context, 'application': application} )

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')
            return render(request, 'admission_app/login.html')
          
    else:
        form = SignupForm()
    return render(request, 'admission_app/signup.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm( request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('admission-profile')
    else:
        u_form = UserUpdateForm( instance = request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'admission_app/profile.html', context)
 

def application(request):

    hide = Application.objects.filter(user=request.user)
    if request.method=="POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()
            application.user = request.user
            application.save()
            return render(request, "admission_app/application.html")
    else:
        form=ApplicationForm()
    return render(request, "admission_app/application.html", { 'form':form,'hide':hide})
