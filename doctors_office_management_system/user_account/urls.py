from django.urls import path
from user_account import views
                   

app_name = 'user_account'

urlpatterns = [
    path('follow/', views.following),
    path('comment/', views.comment),
    path('search/keyword=<str:keyword>/', views.search),
    path('setAppointment/', views.set_appointment),
    path('showTimes/day=<str:day>/date=<str:date>/id=<int:doctorID>/', views.show_times)
]