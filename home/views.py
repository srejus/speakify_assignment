from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse

from accounts.models import UserProfile,Interest

# Create your views here.
class IndexView(View):
    def get(self,request):
        if not request.user.is_authenticated:
            return redirect('/login')
        
        interests = request.user.interest.values_list('id', flat=True)
        users = UserProfile.objects.filter(is_online=True,interest__in=interests).exclude(id=request.user.id)
        return render(request,'index.html',{'users':users})
    

class ToggleOnlineView(View):
    def get(self,request):
        if not request.user.is_authenticated:
            return redirect('/login')
        
        state = request.GET.get('state')
        user = UserProfile.objects.filter(id=request.user.id).first()
        if state == 'on':
            user.is_online = True
        elif state == 'off':
            user.is_online = False
        
        user.save()
        return redirect('/')