from django.shortcuts import render, redirect
from django.views import View
from .models import Event
import json
from datetime import datetime, timedelta
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.core.mail import send_mail


def get_upcoming_events():
    current_date = datetime.now().date()
    one_day_later = current_date + timedelta(days=1)
    upcoming_events = Event.objects.filter(start__lte=one_day_later)
    return upcoming_events



class CalendarView(View):
    def get(self, request, *args, **kwargs):
        if 'logout' in request.GET:
            logout(request)
        events = Event.objects.all()
        upcoming_events = get_upcoming_events()
        print('=================')
        user = request.user
        if user.is_authenticated:
            if upcoming_events.exists():
                for i in upcoming_events:
                    description = i.description
                    title = i.title

                send_mail(f'Напоминание о завтрашнем мероприятии { title }', description , settings.EMAIL_HOST_USER, [user.email])
                print('SSSSSSUUUUUUUUUCCCCCCEEEEESSSSSSs')
            else:
                print('aaaaaaaaaaaaaa')
                print('=================')
        name = request.user.username
        return render(request, 'events/calendar.html', context={'events': events, 'name':name})

class Login(View):
    def get(self, request):
        return render(request, 'events/login.html')
    
    def post(slef, request):
        if 'signup' in request.POST:
                
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = User.objects.create_user(username=name, password=password, email=email)
            login(request, user)

            return redirect('/')
    
        if 'login' in request.POST:
            user = request.POST.get('name')
            password = request.POST.get('password')
            user = authenticate(request, username=user, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                error = 'Данные не корректны'
                
                return render(request, 'events/login.html', context={'error':error})