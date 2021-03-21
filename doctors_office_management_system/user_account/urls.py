from django.urls import path
from user_account import views
                   

app_name = 'user_account'

urlpatterns = [
    path('follow/', views.following),
    path('comment/', views.comment),
    path('search/', views.search),
    path('setAppointment/', views.set_appointment),
]