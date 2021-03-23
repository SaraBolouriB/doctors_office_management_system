from django.urls import path
from django.conf.urls import url
from user_account import views
                   

app_name = 'user_account'

urlpatterns = [
    path('follow/', views.following),
    path('comment/', views.comment),
    path('search/keyword=<str:keyword>/', views.search),
    path('setAppointment/', views.set_appointment),
    path('showTimes/day=<str:day>/date=<str:date>/id=<int:doctorID>/', views.show_times),
    path('registerinfo/', views.register_userinfo),
    path('editinfo/user_id=<str:user_id>', views.edit_userinfo),
    path('doctorinfo/doctorid=<str:doctorid>/', views.doctorinfo),
    path('getlist/',views.filter)
]