import hashlib

from django.shortcuts import render,redirect
from django.views import View
from django.http import JsonResponse

from accounts.models import UserProfile,Interest

# Create your views here.
class IndexView(View):
    def get(self,request):
        if not request.user.is_authenticated:
            return redirect('/login')
        
        interests = request.user.interest.values_list('id', flat=True)
        users = UserProfile.objects.filter(is_online=True,interest__in=interests).exclude(id=request.user.id)
        if not users.exists():
            users = UserProfile.objects.filter(is_online=True).exclude(id=request.user.id)
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
    

#  Connection related views
class ConnectionView(View):
    def get(self,request,id=None):
        if not request.user.is_authenticated:
            return redirect('/login')
        if not request.user.is_online:
            return redirect('/')
        user = UserProfile.objects.filter(id=id,is_online=True)
        if not user.exists():
            return redirect('/')
        receiver_user = user.first()
        sender_user = request.user
        raw_chat_room_id = str(receiver_user.id)+str(sender_user.id)
        sorted_chat_room_id = '-'.join(sorted(list(raw_chat_room_id)))
        hash_object = hashlib.sha256(sorted_chat_room_id.encode())
        room_id = hash_object.hexdigest()
        return render(request,'connect.html',{'room_id':room_id,'connected_user':receiver_user})
    
    def post(self,request):
        return JsonResponse({'status': 'ok'})
