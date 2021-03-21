from django.urls import path
from user_account import views
                   

app_name = 'user_account'

urlpatterns = [
    path('follow/', views.following),
    path('comment/', views.comment),
]