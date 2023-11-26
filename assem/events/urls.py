from django.urls import path
from .views import CalendarView,  Login

urlpatterns = [
    path('', CalendarView.as_view(), name='calendar'),
    path('login', Login.as_view(), name='login'),

    
    # Add other URLs as needed
]