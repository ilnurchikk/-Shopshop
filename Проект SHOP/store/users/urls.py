from django.urls import path

from users.views import login, register, profile, logout

app_name = 'users'

#Набор уникальных путей к именам файлов для перехода на отдельные стр

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
path('logout/', logout, name='logout')
]

#02.09.24