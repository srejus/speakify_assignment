from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.shortcuts import render,redirect
from django.views import View

from .countries import countries
from .models import Interest,UserProfile
from .utils import is_valid_email


# Create your views here.
class SignupView(View):
    def get(self,request):
        interests = Interest.objects.all()
        err = request.GET.get('err')
        return render(request,'signup.html',{'interests':interests,'err':err})
    
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('pass1')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        interests = request.POST.getlist('interest')

        # Check if a user with the given email or phone already exists
        if not UserProfile.objects.filter(Q(email=email) | Q(phone=phone)).exists():
            if country and country.lower() not in countries:
                err = 'Invalid country name!'
                return redirect(f'/signup?err={err}')
            if phone and len(phone) < 10:
                err = 'Invalid phone number!'
                return redirect(f'/signup?err={err}')
            
            # Create a new user
            user = UserProfile.objects.create_user(username=email, email=email, password=password)
            user.first_name = name
            user.gender = gender
            user.country = country
            user.phone = phone
            user.save()
            
            # filter Interest objs with interestnames(use id in frontend)

            # Add interests to the user profile
            for interest_obj in interests:
                interest = Interest.objects.get(id=interest_obj)
                user.interest.add(interest)

            return redirect('/login')
        else:
            err = 'User with this email or phone already exists!'
            return redirect(f'/signup?err={err}')
    

class LoginView(View):
    def get(self,request):
        err = request.GET.get('err')
        return render(request,'login.html',{'err':err})

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('pass1')
        
        if username and username.isnumeric():
            user_obj = UserProfile.objects.filter(phone=username).first()
            if not user_obj:
                err = 'Invalid credentials!'
                return redirect(f'/login?err={err}')
            
            original_username = user_obj.username
            user = authenticate(request, username=original_username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        elif username and is_valid_email(username):
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            
        err = 'Invalid credentials!'
        return redirect(f'/login?err={err}')
